'''
You are given a 2D array of characters and a character pattern. 
WAP to find if pattern is present in 2D array. 
Pattern can be in any way (all 8 neighbors to be considered) but you can't use same character twice while matching.
'''

def find2d(a,p):
    n = len(a)
    m = len(a[0])
    for i in xrange(n):
        for j in xrange(m):
            v = []
            if checkaround(a,p,i,j,v):
                return v
    return []

def checkaround(a,p,i,j,v):
    if len(p) == 0:
        return True

    n = len(a)
    m = len(a[0])
    r1 = i-1 if i-1>=0 else 0
    r2 = i+2 if i+1<n  else n
    c1 = j-1 if j-1>=0 else 0
    c2 = j+2 if j+1<m  else m

    for i in xrange(r1,r2):
        for j in xrange(c1,c2):
            if (i,j) not in v:
                if a[i][j] == p[0]:
                    v.append((i,j))
                    return checkaround(a,p[1:],i,j,v)

a = [ ['A','C','P','R','C'],
      ['X','S','O','P','C'],
      ['V','O','V','N','I'],
      ['W','G','F','M','N'],
      ['Q','A','T','I','T'] ]
n = len(a)
m = len(a[0])

p = 'MICROSOFT'

v = find2d(a,p)
print v


'''Pretty printout'''
s = ""
o = ""
for i in xrange(n):
    for j in xrange(m):
        o += ' ' + a[i][j] + ' '
        if (i,j) in v:
            s += ' ' + str(v.index((i,j))+1) + ' '
        else:
            s += '   '
    s += "\n"
    o += "\n"
print s
print o
