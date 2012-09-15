


def spiral(a):

    r1 = c1 = 0
    r2 = len(a)
    c2 = len(a[0])
    r = []

    while r1 < r2 and c1 < c2:
        '''Go right'''
        for i in xrange(c1,c2):
            r.append(a[r1][i])
        r1 += 1
        '''Go down'''
        for j in xrange(r1,r2):
            r.append(a[j][c2-1])
        c2 -= 1
        '''Go left'''
        for k in xrange(c2-1,c1-1,-1):
            r.append(a[r2-1][k])
        r2 -= 1
        '''Go up'''
        for m in xrange(r2-1,r1-1,-1):
            r.append(a[m][c1])
        c1 += 1
            
    return r


a = [ [11,12,13,14], [21,22,23,24], [31,32,33,34], [41,42,43,44] ]

print spiral(a)
