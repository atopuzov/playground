#!/usr/bin/python
# (c) Aleksandar Topuzovic <aleksandar.topuzovic@gmail.com>
import collections

def anagram(s1, s2):
    ds1 = {}
    ds2 = {}

    for x in s1:
        if x in ds1:
            ds1[x] += 1
        else:
            ds1[x] = 1

    for x in s2:
        if x in ds2:
            ds2[x] += 1
        else:
            ds2[x] = 1

    return ds1 == ds2

def anagram2(s1, s2):
    ds1 = collections.defaultdict(lambda: 0)
    ds2 = collections.defaultdict(lambda: 0)

    for x in s1:
        ds1[x] += 1

    for x in s2:
        ds2[x] += 1

    return ds1 == ds2

def anagram3(s1, s2):
    ds1 = collections.Counter(s1)
    ds2 = collections.Counter(s2)
    return ds1 == ds2

if __name__ == '__main__':
    a = 'debit card'
    b = 'bad credit'

    print anagram(a,b)
    print anagram2(a,b)
    print anagram3(a,b)
