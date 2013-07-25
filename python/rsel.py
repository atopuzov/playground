#!/usr/bin/python
# (c) Aleksandar Topuzovic <aleksandar.topuzovic@gmail.com>
import random

def rpartition(elements, p=None):
    '''Partitions the array, if no pivot is specified it uses the median of three method to obtain the pivot'''
    if len(elements) == 0:
        return [], [], []
    if p is None:
        p1 = elements[0]  # First element
        p2 = elements[-1]  # Last element
        p3 = elements[len(elements)/2]  # Middle eleemnt
        pivots = [p1, p2, p3]
        p = sorted(pivots)[1]  # Median of three

    el = [x for x in elements if x < p]  # Less then the pivot
    ee = [x for x in elements if x == p]  # Same as the pivot
    eg = [x for x in elements if x > p]  # Greater then the pivot

    return (el, ee, eg)

def rselect(a, i):
    (el, ee, eg) = rpartition(a)
    less = len(el)
    equal = len(ee)

    if i in range(less, less + equal):
        return ee[0]
    elif i < less:
        return rselect(el, i)
    elif i > less:
        return rselect(eg, i - less - equal)

if True:
    for x in xrange(10000):
        if random.randint(0,1) == 0:
            a = [random.randint(1, 10) for x in range(10)]
        else:
            a = random.sample(xrange(500), random.randint(5,20))
        s = sorted(a)
        h = []
        for l in range(len(a)):
            r = rselect(a, l)
            h.append(r)

        assert(h == s)
