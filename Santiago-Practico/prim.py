class Prim:

    def __init__(self):
        self.graph = {}
        self.nodes = set()
        self.edges = []
        self.mst = []
        self.inf = float("inf")

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
            self.nodes.add(u)
        if v not in self.graph:
            self.graph[v] = {}
            self.nodes.add(v)
        self.graph[u][v] = w
        self.graph[v][u] = w

    def build_graph(self, edges):
        for edge in edges:
            u, v, w = edge
            self.add_edge(u, v, w)
        self.edges = [(u, v, self.graph[u][v]) for u in self.graph for v in self.graph[u]]

    def apply_prim(self):
        visited = {n: False for n in self.nodes}
        keys = {n: self.inf for n in self.nodes}
        parents = {n: None for n in self.nodes}
        keys[next(iter(self.nodes))] = 0
        for i in range(len(self.nodes)):
            min_node = None
            for node in self.nodes:
                if not visited[node] and (min_node is None or keys[node] < keys[min_node]):
                    min_node = node
            visited[min_node] = True
            for adjacent in self.graph[min_node]:
                if not visited[adjacent] and self.graph[min_node][adjacent] < keys[adjacent]:
                    keys[adjacent] = self.graph[min_node][adjacent]
                    parents[adjacent] = min_node
        for u, v in parents.items():
            if v is not None:
                self.mst.append((v, u, self.graph[u][v]))
        return self.mst