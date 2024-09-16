# Se define la función para encontrar el árbol de expansión mínima usando el algoritmo de Prim
def prim(start_node,graph):
    # Lista para almacenar los nodos ya visitados
    visited = set()
    
    # Lista para almacenar las aristas del árbol de expansión mínima
    mst = []
    
    # Comenzar desde el nodo de inicio
    visited.add(start_node)
    
    # Mientras no hayamos visitado todos los nodos
    while len(visited) != len(graph):
        # Lista para almacenar las aristas que conectan nodos visitados con nodos no visitados
        edges = []
        
        # Iterar a través de los nodos visitados
        for node in visited:
            # Iterar a través de las aristas conectadas a este nodo
            for edge in graph[node]:
                # Si el nodo conectado no ha sido visitado, agregar la arista a la lista de aristas
                if edge[0] not in visited:
                    edges.append((node, edge[0], edge[1],))
        
        # Si no hay aristas que conecten nodos visitados con nodos no visitados
        if len(edges) == 0:
           return mst
        
        # Elegir la arista de peso mínimo
        min_edge = min(edges, key=lambda x: x[2])
        
        # Agregar la arista al árbol de expansión mínima y agregar el nodo conectado a los visitados
        
        visited.add(min_edge[1])
        mst.append(min_edge)
    # Retornar el árbol de expansión mínima
    return mst


# Caso de estudio
graph = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 3), ('D', 1)],
    'C': [('B', 3), ('D', 4)],
    'D': [('A', 5), ('B', 1), ('C', 4)]
}

start_node = 'A'
mst = prim(start_node,graph)

print(mst)