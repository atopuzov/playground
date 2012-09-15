
'''Running time log(n)'''
def bs(a,s):
    if len(a) == 1:
        return a[0] == s

    h = len(a)/2
    e = a[h]
    if e == s:
        return True
    elif a < s:
        return bs(a[:h],s)
    else:
        return bs(a[h:],s)

'''Running time n^2'''
def naive(a,s):
    for i in xrange(len(a)-1):
        for j in xrange(i+1,len(a)):
            if a[i] + a[j] == s:
                return True
    return False

'''Running time n*log(n)'''
def better(a,s):
    a.sort()
    for i in xrange(len(a)):
        d = s - a[i]
        if bs(a,d):
            return True
    return False

'''Running time n'''
def better2(a,s):
    h = {}
    for i in xrange(len(a)):
        h[a[i]] = i
    for i in xrange(len(a)):
        if h.get( s-a[i], None):
            return True
    return False

a = [1,3,5,6,8,10,45,23,12,34,23,18,28]
s = 53

print naive(a,s), better(a,s), better2(a,s)
