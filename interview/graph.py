def dfs_r(g,n):
    nodes = g.get(n,[])
    for n in nodes:
        dfs_r(g,n)

def dfs(g,start):
    '''Depth first search'''
    processed = []
    queued = [start]

    while queued:
        n = queued.pop(0)
        processed.append(n)
        new = [c for c in g.get(n,[]) if c not in processed + queued]
        '''For postorder traversal'''
        # new.reverse()
        queued = new + queued

    return processed

def bfs(g,start):
    '''Breadth first search'''
    processed = []
    queued = [start]

    while queued:
        n = queued.pop(0)
        processed.append(n)
        new = [c for c in g.get(n,[]) if c not in processed + queued]
        '''For postorder traversal'''
        # new.reverse()
        queued = queued + new

    return processed

def depth(g,node):
    c = g.get(node,[])
    if not c:
        return 1
    d = [depth(g,n) for n in c]
    return 1 + max(d)

def diametar(g,node):
    c = g.get(node,[])
    if not c:
        return 1
    d = [diametar(g,n) for n in c]
    d2 = [depth(g,n) for n in c]
    d += [1+sum(d2)]
    return max(d)

g = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    5: [7,8],
    6: [9],
    9: [10, 11],
    10: [12, 13],
}
g = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [7,8],
    5: [9],
    8: [10],
    9: [11, 12],
    10: [13, 14],
    12: [15],
}


wg = {
    's':{'u':10, 'x':5},
    'u':{'v':1, 'x':2},
    'v':{'y':4},
    'x':{'u':3, 'v':9, 'y':2},
    'y':{'s':7, 'v':6}
}

def graph_add_undirected(g, e1, e2, w):
    d = g.get(e1, {})
    d[e2] = w
    g[e1] = d

    d = g.get(e2, {})
    d[e1] = w
    g[e2] = d

def graph_delete_undirected(g, e1, e2):
    d = g.get(e1, {})
    del(d[e2])
    g[e1] = d
    
    d = g.get(e2, {})
    del(d[e1])
    g[e2] = d

def prim(g):
    '''Prims Algorithm for minimal spannig tree: http://en.wikipedia.org/wiki/Prim's_algorithm'''
    v = g.keys()
    new_g = {}
    new_v = [v.pop(0)]

    while v:
        connected = []
        for node in new_v:
            connected += [(node,e,g[node][e]) for e in g[node].keys() if e not in new_v]

        e = min(connected, key=lambda x:x[2])
        new_v.append(e[1])
        v.remove(e[1])

        graph_add_undirected(new_g, e[0], e[1], e[2])
    return new_g

def k_find(C,u):
    while C[u] != u:
        u = C[u]
    return u

def k_union(C, u, v):
    u = k_find(C,u)
    v = k_find(C,v)
    C[u] = v

def kruskal(g):
    '''Kruskal's algorithm for minimum spanning tree: http://en.wikipedia.org/wiki/Kruskal%27s_algorithm'''
    v = g.keys()
    new_g = {}

    edges = []
    for node in v:
        edges += [(node,e,g[node][e]) for e in g[node].keys()]
    edges.sort(key=lambda x:x[2])
    C = {u:u for u in v}
    for e in edges:
        if k_find(C,e[0]) != k_find(C,e[1]):
            k_union(C, e[0], e[1])
            graph_add_undirected(new_g, e[0], e[1], e[2])

    return new_g

gp = {
    'A': {'B':7, 'D':5},
    'B': {'A':7, 'C':8, 'D':9, 'E':7},
    'C': {'B':8, 'E':5},
    'D': {'A':5, 'B':9, 'E':15, 'F':6},
    'E': {'C':5, 'B':7, 'D':15, 'F':8, 'G':9},
    'F': {'D':6, 'E':8, 'G':11},
    'G': {'F':11, 'E':9},
}

# print "DFS:", dfs(wg, 's')
# print "BFS:", bfs(wg, 's')
# print "DFS:", dfs(g, 1)
# print "BFS:", bfs(g, 1)
print depth(g,1), diametar(g,1)

# print "Graph:", gp, "\n"
# print "Kruskal:", kruskal(gp), "\n"
# print "Prim:", prim(gp), "\n"


