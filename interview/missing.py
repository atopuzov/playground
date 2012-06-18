from __future__ import division
from math import factorial

def missing(a):
    n = len(a)
    s2 = n*(n+1)/2
    ss2 = n*(n+1)*(2*n+1)/6
    s1 = sum(a)
    ss1 = sum([x**2 for x in a])
    d1 = s2 - s1
    d2 = ss2 - ss1
    missing = (d2+d1)/2
    duplicate = (d2-d1)/2
    return missing, duplicate

def missing2(a):
    n = len(a)
    s2 = n*(n+1)/2
    m2 = factorial(n)
    s1 = sum(a)
    m1 = reduce(lambda x,y: x*y, a)
    d1 = s2-s1
    d2 = m1/m2
    missing = d1/(1.0-d2)
    duplicate = missing-d1
    return missing, duplicate


a = [1,2,3,4,5,5,7]

m,d = missing(a)
m2,d2 = missing2(a)
print "Array: ", a
print "Missing:", m, ", duplicate:", d
print "Missing:", m2, ", duplicate:", d2
