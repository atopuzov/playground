#!/usr/bin/env python
# (c) 2013 Aleksandar Topuzovic <aleksandar.topuzovic@gmail.com>
import collections
import json
import os.path
import sys

if __name__ == '__main__':
    wl = collections.defaultdict(lambda: [])

    if not os.path.exists('cache.json'):
        print "Creating cache ..."
        with open('wordsEn.txt') as f:
            for line in f.readlines():
                word = line.strip()
                l = len(word)
                c = collections.Counter(list(word))
                wl[l].append((word,c))

        with open('cache.json','w') as f:
            f.write(json.dumps(wl, indent=4))

    with open('cache.json') as f:
        wl = json.loads(f.read())

        try:
            input = sys.argv[1]
        except IndexError:
            input = 'love'

        input = list(input)
        l = str(len(input))
        c = collections.Counter(input)

        print "Anagrams:", ', '.join([x[0] for x in wl[l] if x[1] == c])
