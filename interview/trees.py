
class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        l = str(self.left.data) if self.left else ""
        r = str(self.right.data) if self.right else ""
        d = str(self.data) if self.data else ""
        s = "%s |%s| %s" % (l,d,r)
        s = str(d)
        return s


rt = node('root')
l = node('l')
r = node('r')

rt.left = l
rt.right = r

a = [9,3,7,1,8,12,10,20,15,18,5]

def dfs(n):
    q = [n]
    l = []
    k = []
    while q:
        v = q.pop(0)
        if v.right:
            q = [v.right] + q
        if v.left:
            q = [v.left] + q
        l += [v]
        k = [v] + k
    # preorder
    print l
    # postorder
    print k

def dfs_r(n):
    if not n:
        return []
    if not n.left and not n.right:
        return [n]
    else:
        return [n] + dfs_r(n.left) + dfs_r(n.right)

def bfs(n):
    q = [n]
    l = []
    k = []
    while q:
        v = q.pop(0)
        if v.left:
            q = q + [v.left]
        if v.right:
            q = q + [v.right]
        l += [v]
        k = [v] + k
    # preorder
    print l
    # postorder
    print k

def create_cartesian_tree(a):
    if len(a) == 0:
        return None
    elif len(a) == 1:
        return node(a[0])
    else:
        m = a.index(min(a))
        r = node(a[m])
        r.left = create_cartesian_tree(a[:m])
        r.right = create_cartesian_tree(a[m+1:])
        return r

# t = create_cartesian_tree(a)
# dfs(t)
# bfs(t)
# k = dfs_r(t)
# print k

n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)
n6 = node(6)
n7 = node(7)
n8 = node(8)
n9 = node(9)
n10 = node(10)
n11 = node(11)
n12 = node(12)
n13 = node(13)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n7
n5.right = n8
n3.right = n6
n6.right = n9
n9.left = n10
n9.right = n11
n10.left = n12
n10.right = n13

def tree_depth(n):
    if not n:
        return 0
    return 1 + max( tree_depth(n.left), tree_depth(n.right) )

def tree_diametar(n):
    if not n:
        return 0
    return max( 1 + tree_depth(n.left) + tree_depth(n.right), tree_diametar(n.left), tree_diametar(n.right))

print tree_diametar(n1)

