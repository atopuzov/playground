
def setZero(a):
    rows = []
    cols = []
    n = len(a)
    m = len(a[0])
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for r in rows:
        for j in xrange(m):
            a[r][j] = 0

    for c in cols:
        for i in xrange(n):
            a[i][c] = 0
    return a

a = [ [1,2,3],
      [1,0,3],
      [1,2,4],
      [3,4,5] ]

print a, "\n", setZero(a)

