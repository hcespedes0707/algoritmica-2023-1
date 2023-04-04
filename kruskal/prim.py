class Prim:

    def __init__(self):
       # Inicializamos las variables
        self.met = []               # Lista donde se guardarán las aristas que conforman el árbol de expansión mínima (MST)
        self.nodes = {}             # Diccionario donde se guardarán los nodos y sus adyacencias
        self.visited = {}           # Diccionario para llevar registro de los nodos visitados
        self.edges = []             # Lista de prioridad para ordenar las aristas por peso
        self._origin = 0            # Índice para el origen de la arista en la lista de adyacencias
        self._destination = 1       # Índice para el destino de la arista en la lista de adyacencias
        self._weight = 2            # Índice para el peso de la arista en la lista de adyacencias

    def apply_prim(self, nodes, edges):
        # Construimos el grafo
        self.build_graph(nodes, edges)
        # Seleccionamos el nodo de inicio
        start_node = nodes[0]
        self.process_node(start_node)
        # Recorremos el grafo
        while len(self.edges) > 0:
            # Tomamos la arista de menor peso
            min_edge = None
            for edge in self.edges:
                if min_edge is None or edge[2] < min_edge[2]:
                    min_edge = edge
            self.edges.remove(min_edge)
            origin, destination, weight = min_edge
            if not self.visited[destination]:
                self.met.append(min_edge)
                self.process_node(destination)
        sorted_met = sorted(self.met, key=lambda x: x[self._weight])
        return sorted_met
    
    
    def get_weight(self, node):
        return node[2]


    def build_graph(self, nodes, edges):
        # Construimos el grafo, llenando los nodos
        # como no visitados
        for node in nodes:
            self.nodes[node] = [] # Inicializamos la lista de adyacencias de cada nodo
            self.visited[node] = False #Todos los nodos son no visitados
        for edge in edges:
            origin, destination, weight = edge # Obtenemos los valores de la arista
            # Agregamos la arista a las listas de adyacencia de los nodos correspondientes
            self.nodes[origin].append((destination, weight))
            self.nodes[destination].append((origin, weight))

    def process_node(self, node):
        self.visited[node] = True
        for adj_node in self.nodes[node]:
            if not self.visited[adj_node[0]]:
                self.edges.append((node, adj_node[0], adj_node[1]))

    