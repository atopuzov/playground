def permute_recursive(a):
    if type(a) != type([]):
        return

    if len(a) == 0:
        return []
    elif len(a) == 1:
        return a
    elif len(a) == 2:
        p1 = [a[0]] + [a[1]]
        p2 = [a[1]] + [a[0]]
        return [p1,p2]
    else:
        p = []
        for i in range(len(a)):
            for s in permute_recursive(a[:i] + a[i+1:]):
                p.append( [a[i]] + s )
        return p

def permute_iterative(a):
    if type(a) != type([]):
        return

    results = []
    results.append(a[:])
    # yield a[:]

    N = len(a)

    p = list(xrange(N+1))
    i = 1
    while i<N:
            p[i]-=1
            
            j = p[i] * (i % 2)
            a[j], a[i] = a[i], a[j]
            results.append(a[:])
            # yield a[:]

            i = 1
            while not p[i]:
                p[i] = i
                i+=1
    return results

l = [1,2,3]
print permute_iterative(l)
print permute_recursive(l)
