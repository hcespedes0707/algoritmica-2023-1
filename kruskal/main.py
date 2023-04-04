from kruskal import *;
from prim import *;



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
    prim = Prim()
    metw = prim.apply_prim(nodes, edges)
    print("Kruskal: ",met)
    print("Prim:    ",metw)

