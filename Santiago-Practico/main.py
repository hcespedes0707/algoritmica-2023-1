from kruskal import Kruskal
from prim import Prim

nodes = ['a','b','c','d','e','f', 'g']
edges = [
    ('a', 'b', 7),
    ('b', 'c', 8),
    ('c', 'e', 5),
    ('e', 'g', 9),
    ('g', 'f', 11),
    ('d', 'f', 6),
    ('a', 'd', 5),
    ('d', 'b', 9),
    ('d', 'e', 15),
    ('b', 'e', 7),
    ('e', 'f', 8)
]

if __name__ == '__main__':
    kruskal = Kruskal()
    met = kruskal.apply_kruskal(nodes, edges)
    print(met)

    prim = Prim()
    prim.build_graph(nodes, edges)
    result = prim.prim()
    result = sorted(result, key=lambda node: node[2])
    print(result)