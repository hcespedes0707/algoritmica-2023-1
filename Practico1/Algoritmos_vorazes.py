class Algoritmos_vorazes:

    def __init__(self):
        self.met = []
        self.result = []
        self.visited = []
        self.nodes = {}
        self.level = {}
        self._origin = 0
        self._destination = 1
        self._weight = 2

    def get_weight(self, node):
        return node[2]

    def sort_graph(self, graph):
        # Estructura del grafo (origen, destino, peso) --> ('A', 'D',  5)
        return sorted(graph, key=lambda node: node[self._weight])

    def initialize_data(self, node):
        self.nodes[node] = node
        self.level[node] = 0
        # En el caso de los visitados, almacenamos el nivel y en los nodos los conjuntos

    def find_set_root(self, node):
        # Buscamos el nodo raiz del conjunto, si el valor no es el mismo: buscamos sobre el padre
        if self.nodes[node] != node:
            # Aca el metodo se hace recursivo para llegar hasta el nivel 0
            self.nodes[node] = self.find_set_root(self.nodes[node])
        return self.nodes[node]

    def check_union(self, origin, destination):
        # Lo primero que vamos a hacer es encontrar los nodos raiz de ambos nodos
        origin_found = self.find_set_root(origin)
        destination_found = self.find_set_root(destination)
        # Solo seguiremos adelante si los nodos raiz son diferentes
        if origin_found != destination_found:
            # Si el nivel del nodo origen es mayor al del destino, entonces el destino se une al origen
            if self.level[origin_found] > self.level[destination_found]:
                self.nodes[destination_found] = origin_found
            # Si el nivel del nodo destino es mayor al del origen, entonces el origen se une al destino
            elif self.level[origin_found] < self.level[destination_found]:
                self.nodes[origin_found] = destination_found
            # Si ambos nodos tienen el mismo nivel, entonces el destino se une al origen y el nivel del origen aumenta
            else:
                self.nodes[destination_found] = origin_found
                self.level[origin_found] += 1

    def apply_kruskal(self, nodes, edges):
        # Preparamos la informacion
        for node in nodes:
            self.initialize_data(node)
        # Ordeno el grafo
        sorted_edges = self.sort_graph(self.sort_graph(edges))
        # Agregamos el primer nodo a la solucion
        self.met.append(sorted_edges.pop(0))
        # Agregamos el primer nodo a los visitados
        self.visited.append(self.met[0][self._origin])
        # Recorremos el grafo
        while sorted_edges:
            # Obtenemos el nodo de menor peso
            node = sorted_edges.pop(0)
            # Verificamos si el nodo destino se encuentra en los visitados
            if node[self._destination] not in self.visited:
                # Si no esta en los visitados, lo agregamos
                self.visited.append(node[self._destination])
                # Agregamos el nodo a la solucion
                self.met.append(node)
            # Verificamos si el nodo origen se encuentra en los visitados
            elif node[self._origin] not in self.visited:
                # Si no esta en los visitados, lo agregamos
                self.visited.append(node[self._origin])
                # Agregamos el nodo a la solucion
                self.met.append(node)
        return self.met

    def apply_prim(self, nodes, edges):
        # Se inicializan las variables del algoritmo
        self.nodes = {}
        self.level = {}
        self.met = []
        self.visited = []
        self.result = []
        # Se inicializan los nodos y el nivel
        for node in nodes:
            self.initialize_data(node)
        # Se ordena la lista de aristas según el peso
        sorted_edges = self.sort_graph(edges)
        # Se agrega el primer nodo a la lista de visitados
        self.visited.append(nodes[0])
        # Mientras queden nodos sin visitar
        while len(self.visited) != len(nodes):
            # Se busca la arista de menor peso que conecte un nodo visitado con uno no visitado
            for edge in sorted_edges:
                if edge[self._origin] in self.visited and edge[self._destination] not in self.visited:
                    self.result.append(edge)
                    self.check_union(edge[self._origin], edge[self._destination])
                    self.met.append(edge)
                    self.visited.append(edge[self._destination])
                    break
        return self.result
        
    