import sys 

class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.MST = []
        
    def printSolution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s : %s" % (s, d, w))
    
    # Time complexity - O(V^3) if you represent it using an adjancency list - O(V)
    # Time complexity - O(V) we are inserting V number of vertices to the minimum spanning tree
    def primsAlgo(self):
        visited = [0] * self.vertexNum
        edgeNum = 0
        visited[0] = True
        while edgeNum < self.vertexNum - 1:
            min = sys.maxsize
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if ((not visited[j]) and self.edges[i][j]):
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                source = i
                                destination = j
            self.MST.append([self.nodes[source], self.nodes[destination], self.edges[source][destination]])
            visited[destination] = True
            edgeNum += 1 
        self.printSolution()

edges = [
    [0, 10, 20, 0, 0], 
    [10, 0, 30, 5, 0], 
    [20, 30, 0, 15, 6], 
    [0, 5, 15, 0, 8], 
    [0, 0, 6, 8, 0], 
         ]

nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.primsAlgo()