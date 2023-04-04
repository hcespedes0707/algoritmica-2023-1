from Algoritmos_vorazes import Algoritmos_vorazes

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
    Algoritmos_vorazes = Algoritmos_vorazes()
    met = Algoritmos_vorazes.apply_kruskal(nodes, edges)
    result = Algoritmos_vorazes.apply_prim(nodes, edges)
    print(met)
    print(result)


