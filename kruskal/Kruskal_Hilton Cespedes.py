# Definición del grafo
grafo = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('C', 3), ('D', 1)],
    'C': [('B', 3), ('D', 4)],
    'D': [('A', 5), ('B', 1), ('C', 4)]
}

# Función para encontrar el padre de un vértice
def encontrar_padre(padres, vertice):
    if padres[vertice] == vertice:
        return vertice
    return encontrar_padre(padres, padres[vertice])

# Función para unir dos subconjuntos en uno solo
def unir_subconjuntos(padres, rango, vertice1, vertice2):
    raiz1 = encontrar_padre(padres, vertice1)
    raiz2 = encontrar_padre(padres, vertice2)

    if rango[raiz1] < rango[raiz2]:
        padres[raiz1] = raiz2
    elif rango[raiz1] > rango[raiz2]:
        padres[raiz2] = raiz1
    else:
        padres[raiz2] = raiz1
        rango[raiz1] += 1

# Función que implementa el algoritmo de Kruskal
def kruskal(grafo):
    # Inicialización de variables
    arbol_expansion = []
    padres = {}
    rango = {}

    # Inicialización de padres y rango
    for vertice in grafo:
        padres[vertice] = vertice
        rango[vertice] = 0

    # Ordenamos todas las aristas del grafo por peso de menor a mayor
    aristas_ordenadas = sorted([(peso, vertice1, vertice2) for vertice1 in grafo for vertice2, peso in grafo[vertice1]])

    # Recorremos todas las aristas ordenadas y unimos los subconjuntos
    for arista in aristas_ordenadas:
        peso, vertice1, vertice2 = arista
        if encontrar_padre(padres, vertice1) != encontrar_padre(padres, vertice2):
            unir_subconjuntos(padres, rango, vertice1, vertice2)
            arbol_expansion.append(arista)

    # Retornamos el árbol de expansión mínimo
    return arbol_expansion

# Ejecutamos el algoritmo de Kruskal y mostramos el resultado
arbol_expansion = kruskal(grafo)
print(arbol_expansion)