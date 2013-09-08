#!/usr/bin/env python
# (c) Aleksandar Topuzovic <aleksandar.topuzovic@gmail.com>
from collections import namedtuple, defaultdict
from random import sample
from logging import info, root
from itertools import chain

def prim(graph):
    '''
    Primms algorithm for getting the minimum spanning tree
    '''
    vertices = graph.keys()
    random_vertex = sample(vertices, 1)[0]
    info("Selected vertex: {}".format(random_vertex))

    x = {random_vertex}
    t = []
    while x != set(g.keys()):
        info("X = {}".format(", ".join(x)))
        # All edges from vertrices from X
        all_edges = chain.from_iterable([g[r] for r in x])
        # Select edges such that dst is not in X
        considered_edges = [_edge for _edge in all_edges if _edge.dst not in x]
        info("Considered edges: {}".format(", ".join([str(_edge) for _edge in considered_edges])))
        # Select the edge with minimum cost
        least_cost_edge = min(considered_edges, key=lambda e: e.cost)
        info("Least cost edge: {}".format(least_cost_edge))
        t.append(least_cost_edge)
        x.add(least_cost_edge.dst)
    return t

def construct_tree_from_edges(edges):
    '''
    Builds a tree from edges
    '''
    tree = defaultdict(list)
    for _edge in edges:
        tree[_edge.src].append(_edge.dst)
        tree[_edge.dst].append(_edge.src)
    return dict(tree)

def build_a_graph(edges):
    '''
    Builds a undirected graph from connecitons
    '''
    edge = namedtuple('edge', 'src dst cost')
    graph = defaultdict(list)
    for _edge in edges:
        src = _edge[0]
        dst = _edge[1]
        cost = _edge[2]
        edge1 = edge(src, dst, cost)
        edge2 = edge(dst, src, cost)
        graph[src].append(edge1)
        graph[dst].append(edge2)
    return dict(graph)
        
if __name__ == '__main__':
    root.setLevel(0)
    e = [('a', 'b', 1), ('a', 'c', 4), ('a', 'd', 3), ('b', 'd', 2), ('c', 'd', 5)]
    g = build_a_graph(e)
    print construct_tree_from_edges(prim(g))
    