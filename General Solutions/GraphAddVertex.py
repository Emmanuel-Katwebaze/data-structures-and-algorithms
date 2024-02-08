class Graph:
    def __init__(self):
        self.adjacencyList = {}
    
    def addVertex(self, vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []