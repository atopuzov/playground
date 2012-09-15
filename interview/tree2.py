def create_bst(seq):
    T = []
    for e in seq:
        insert_bst(T,e)
    return T

def insert_bst(T, e, rb=False):
    if T == []:
        T.append(e)
        T.append([])
        T.append([])
        if rb:
            T.append('R')
        return
    if e < T[0]:
        insert_bst(T[1], e)
    else:
        insert_bst(T[2], e)

def delete_bst(T, e, P=[]):
    if T == []:
        return

    if T[0] == e:
        if T[1] == [] and T[2] == []:
            '''No children'''
            if P != []:
                if P[1] == T:
                    P[1] = []
                elif P[2] == T:
                    P[2] = []
        elif T[1] == []:
            '''Only right child'''
            if P != []:
                if P[1] == T:
                    P[1] = T[2]
                elif P[2] == T:
                    P[2] = T[2]
        elif T[2] == []:
            '''Only left child'''
            if P != []:
                if P[1] == T:
                    P[1] = T[1]
                elif P[2] == T:
                    P[2] = T[1]
        else:
            '''Left and right children'''
            # pred = find_max(T[1])
            # T[0] = pred
            # delete_bst(T[1],pred,P=T)

            succ = find_min(T[2])
            T[0] = succ
            delete_bst(T[2],succ,P=T)

    elif e < T[0]:
        delete_bst(T[1], e, P=T)
    else:
        delete_bst(T[2], e, P=T)

def walk_bst(T, t=0):
    n = []
    if T == []:
        return []
    if t == 0:
        n += walk_bst(T[1])
        n += [ T[0] ]
        n += walk_bst(T[2])
    elif t == 1:
        n += [ T[0] ]
        n += walk_bst(T[1])
        n += walk_bst(T[2])
    elif t == 2:
        n += walk_bst(T[1])
        n += walk_bst(T[2])
        n += [ T[0] ]
    return n

def find_parent(T, e, P=[]):
    if T == []:
        return

    if e == T[0]:
        return P
    if e < T[0]:
        return find_parent(T[1], e, P=T)
    else:
        return find_parent(T[2], e, P=T)
    return []
    

def find_min(T):
    '''Finds the minimum elelemnt in BST'''
    if T == []:
        return
    while T[1] != []:
        T = T[1]
    return T[0]

def find_max(T):
    '''Finds the maximum element in BST'''
    if T == []:
        return
    while T[2] != []:
        T = T[2]
    return T[0]

def rotate_right(T,e):
    if T == []:
        return
    while T[0] != e:
        if e < T[0]:
            T = T[1]
        elif e > T[0]:
            T = T[2]
    N = create_bst([ T[1][0], T[0] ])

    N[1] = T[1][1]
    N[2][1] = T[1][2]
    N[2][2] = T[2]
    return N

def bfs(T):
    if T == []:
        return []

    Q = [T]
    L = []
    while Q:
        T = Q.pop(0)
        if T[1] != []:
            Q.append(T[1])
        if T[2] != []:
            Q.append(T[2])
        L.append(T[0])

    return L
    
    
# a = [8,3,10,1,6,14,4,7,13]

# T = create_bst(a)
# print T
# print "Minimum:", find_min(T)
# print "Maximum:", find_max(T)
# print walk_bst(T)
# delete_bst(T,8)
# print T
# print walk_bst(T)
# e = 8
# print "Parent of:",e, find_parent(T, e)

a = [4, 3, 5, 1, 2]
T = create_bst(a)
print T
print walk_bst(T)
N = rotate_right(T,1)
print N
print "BFS:", bfs(N), bfs(T)
print walk_bst(N)

