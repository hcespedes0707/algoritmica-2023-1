class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []
    def get_weight(self, node):
        return node[2]

    def test(self):
        testing_list = [('B', 'C', 8),('z', 'D', 5)]#,6,9,7,1,3]
        sorted_list = sorted(testing_list, key=self.get_weight)
        # sorted_list = sorted(testing_list, key=lambda tupla: tupla[2])
        return sorted_list
    

if __name__ == "__main__":
    graph = Graph()
    for item in graph.test():
        print(item)