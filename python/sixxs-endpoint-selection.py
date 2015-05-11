#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The MIT License (MIT)

# Copyright (c) 2014 Aleksandar Topuzović <aleksandar.topuzovic@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import Queue
import StringIO
import lxml.html
import re
import requests
import subprocess
import sys
import threading


PING_COUNT=2
TOP_N_SERVERS=3
SIXXS_POPS = 'https://www.sixxs.net/pops/'
ping_status = re.compile(r'=\s(?P<min>[\d\.]+)/(?P<avg>[\d\.]+)/(?P<max>[\d\.]+)/(?P<mdev>[\d\.]+)\s')


def parse_sixxs_pops():
    html = requests.get(SIXXS_POPS).text
    parsed_html = lxml.html.parse(StringIO.StringIO(html))
    return (pop.text for pop in parsed_html.xpath('/html/body/table/tr/td/div[2]/table[1]/tr/td[4]/a'))


def get_endpoints():
    pops = parse_sixxs_pops()
    return ("{}.sixxs.net".format(pop) for pop in pops)


def ping(ip):
    proc = subprocess.Popen(['ping', '-c{}'.format(PING_COUNT), ip],  stderr=subprocess.STDOUT,
                            stdout=subprocess.PIPE)
    proc.wait()
    out = proc.stdout.read()
    match = ping_status.search(out)

    if match:
        return float(match.group('avg'))
    else:
        return sys.maxint


def pinger(input, output):
    while True:
        ip = input.get()
        output[ip] = ping(ip)
        input.task_done()


if __name__ == '__main__':
    queue = Queue.Queue()
    results = {}

    for _ in range(10):
        worker = threading.Thread(target=pinger, args=(queue, results))
        worker.setDaemon(True)
        worker.start()

    for ip in get_endpoints():
        queue.put(ip)

    queue.join()

    # Printout
    for ip in sorted(results, key=results.__getitem__)[:TOP_N_SERVERS]:
        print "{} latency {}".format(ip, results[ip])

#
# sixxs-endpoint-selection.py ends here
