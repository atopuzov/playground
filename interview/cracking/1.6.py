def rotateImage(a):
    n = len(a)

    for layer in xrange(0,n/2):
        first = layer
        last = n - 1 - layer
        for i in xrange(first, last):
            offset = i - first
            top = a[first][i]
            # left -> top
            a[first][i] = a[last-offset][first]
            # bottom -> left
            a[last-offset][first] = a[last][last-offset]
            # right -> bottom
            a[last][last-offset] = a[i][last]
            # top -> right
            a[i][last] = top
    return a


x =  [ [1,2],
       [3,4] ]

a = [ ['a', 'a', 'a'],
      ['b', 'b', 'b'],
      ['c', 'c', 'c'] ]

b = [ ['a', 'a', 'a', 'a'],
      ['b', 'b', 'b', 'b'],
      ['c', 'c', 'c', 'c'],
      ['d', 'd', 'd', 'd'] ]

print rotateImage(x),rotateImage(a),rotateImage(b)
