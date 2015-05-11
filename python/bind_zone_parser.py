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
'''
The following code servers as an example BIND zone parser
'''

from pyparsing import (Group, Combine, Word, Regex, Literal, Optional, ZeroOrMore, OneOrMore, Suppress, Keyword,
                       dblQuotedString, removeQuotes, alphanums, restOfLine, stringEnd, lineEnd, nums)
from pyparsing import ParseException
import sys


ipAddress = Combine(Word(nums) + ('.' + Word(nums))*3)
toEndOfLine = Combine(restOfLine + lineEnd)

comment = Suppress(Regex(r";(\\\n|.)*").setName('comment')('comment'))
optional_comment = Optional(comment)

number = Word(nums).setParseAction(lambda s, l, t: int(t[0]))
dns_name = Word(alphanums + '._-@*')

special_comment = Suppress(Optional(Literal(';')) +
                           restOfLine +
                           lineEnd)

# ORIGIN directive
origin = (Suppress(Keyword('$ORIGIN')) +
          dns_name('origin') +
          optional_comment)

# TTL directive
ttl = (Suppress(Keyword('$TTL')) +
       number('ttl') +
       optional_comment)

_class = (Suppress(Keyword('IN') |
                   Keyword('HS') |
                   Keyword('CH')).setName('Protocol family'))
_class = Suppress(Keyword('IN'))

# SOA record
# http://www.zytrax.com/books/dns/ch8/soa.html
soaRecordInfo = (number('sn')  + optional_comment +
                 number('ref') + optional_comment +
                 number('ret') + optional_comment +
                 number('ex')  + optional_comment +
                 number('min') + optional_comment)

soaRecord = (soaRecordInfo |
             (Suppress(Literal('(')) +
              soaRecordInfo +
              Suppress(Literal(')'))))

recordSOA = (Suppress(Keyword('SOA')) +
             dns_name('name_server') +
             dns_name('email_addr') +
             soaRecord +
             optional_comment)

# NS record
# http://www.zytrax.com/books/dns/ch8/ns.html
recordNS = (Suppress(Keyword('NS')) +
            dns_name('name_server') +
            optional_comment)

# A record
# http://www.zytrax.com/books/dns/ch8/a.html
recordA  = (Suppress(Keyword('A')) +
            ipAddress('address') +
            optional_comment)

# CNAME record
# http://www.zytrax.com/books/dns/ch8/cname.html
recordCNAME = (Suppress(Keyword('CNAME')) +
               dns_name('canonical_name') +
               optional_comment)

# TXT record
# http://www.zytrax.com/books/dns/ch8/txt.html
txtRecord = ((Suppress(Literal('(')) +
              OneOrMore(dblQuotedString.setParseAction(removeQuotes)) +
              Suppress(Literal(')'))) ^
             OneOrMore(dblQuotedString.setParseAction(removeQuotes)))

recordTXT = (Suppress(Keyword('TXT')) +
             txtRecord('text') +
             optional_comment)

# MX Record
# http://www.zytrax.com/books/dns/ch8/mx.html
recordMX = (Suppress(Keyword('MX')) +
            number('preference') +
            dns_name('mail_exchanger') +
            optional_comment)

# RP Record
recordRP = (Suppress(Keyword('RP')) +
            dns_name +
            dns_name +
            optional_comment)

# PTR Record
# http://www.zytrax.com/books/dns/ch8/ptr.html
recordPTR = (Suppress(Keyword('PTR')) +
             dns_name('name') +
             optional_comment)

# SRV Record
# http://www.zytrax.com/books/dns/ch8/srv.html
recordSRV = (Suppress(Keyword('SRV')) +
             number('priority') +
             number('weight') +
             number('port') +
             dns_name('target') +
             optional_comment)

# LOC Record
recordLOC = (Suppress(Keyword('LOC')) +
             toEndOfLine)

# NAPTR Record
recordNAPTR = (Suppress(Keyword('NAPTR')) +
               toEndOfLine)

preRecord = ((dns_name('owner') + _class) |
             dns_name('owner'))

recordA_     = Group(recordA |
                     (preRecord +
                      recordA))('A')

recordSOA_   = Group(recordSOA |
                     (preRecord +
                      recordSOA))('SOA')

recordNS_    = Group(recordNS |
                     (preRecord +
                      recordNS))('NS')

recordMX_    = Group(recordMX |
                     (preRecord +
                      recordMX))('MX')

recordCNAME_ = Group(recordCNAME |
                     (preRecord +
                      recordCNAME))('CNAME')

recordTXT_   = Group(recordTXT |
                     (preRecord +
                      recordTXT))('TXT')

recordSRV_   = Group(recordSRV |
                     (preRecord +
                      recordSRV))('SRV')

recordPTR_   = Group(recordPTR |
                     (preRecord +
                      recordPTR))('PTR')

recordRP_    = Group(recordRP |
                     (preRecord +
                      recordRP))('RP')

recordLOC_   = Group(recordLOC |
                     (preRecord +
                      recordLOC))('LOC')

recordNAPTR_ = Group(recordNAPTR |
                     (preRecord +
                      recordNAPTR))('NAPTR')

record = (recordA_ ^
          recordSOA_ ^
          recordNS_ ^
          recordMX_ ^
          recordCNAME_ ^
          recordTXT_ ^
          recordSRV_ ^
          recordPTR_ ^
          recordRP_ ^
          recordLOC_ ^
          recordNAPTR_)

lines = (Group(origin | ttl)('DIRECTIVE') |
         comment |
         record)

zoneParser = ZeroOrMore(lines)('zone') + stringEnd

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: {} <zone_file>".format(sys.argv[0])
        sys.exit(-1)

    zone_file = sys.argv[1]

    try:
        tokens = zoneParser.parseFile(zone_file)
        print tokens.asXML()
    except ParseException:
        raise
