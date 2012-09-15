

def mergedIntervals(t):
    h = [False]*100
    for i,j in t:
        for x in xrange(i,j+1):
            h[x] = True
    start = False
    s1 = []
    s2 = []
    
    for i in range(len(h)):
        if h[i] and not start:
            s1.append(i)
            start = True
        if not h[i] and start:
            s2.append(i-1)
            start = False
    n = []
    for b,e in zip(s1,s2):
        n.append((b,e))
    return n

def mi(t,a):
    # t.sort()
    r = []
    mf = False
    for b,e in t:
        if b < a[1] and a[0] < e:
            b1 = b if b<a[0] else a[0]
            e1 = a[1] if e<a[1] else e
            a = (b1,e1)
            continue
        if b > a[1]:
            r.append(a)
            mf = True
        r.append((b,e))
    if not mf:
        r.append(a)
    return r


i1 = [ (1,4), (6,10), (14, 19) ] 
ai1 = (13, 17)
# (1,4) (6,10) (13,19)
i2 = [ (1,5), (6, 15), (20, 21), (23, 26), (27, 30), (35, 40) ] 
ai2 = (14,33)
# (1,5) (6, 33) (35, 40)

# print mergedIntervals(i1+[ai1]) , "\n" , mergedIntervals(i2+[ai2])

print mi(i1, ai1)
print mi(i2, ai2)
