def naive(n):
    if n == 1 or n == 2:
        return True
    for i in xrange(2,n/2+1):
        if n%i == 0:
            return False
    return True

tc = {
    1: True,
    2: True,
    3: True,
    4: False,
    5: True,
    6: False,
    11: True,
    13: True,
    15: False,
    20: False,
    151: True,
    1289: True,
    1300: False,
    1601: True
}

for k,v in tc.items():
    if naive(k) != v:
        print "Error:", k, v
