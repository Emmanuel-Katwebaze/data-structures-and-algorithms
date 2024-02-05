# Used for single source shortest path problem and all pairs shortest path problem
# APSPP - involves running SSSPP for all vertices

class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
    
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
        
    def addNode(self, value):
        self.nodes.append(value)
    
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print(' ' + key, ':   ', value)
    
    # Time complexity - O(VE)
    # Space complexity - O(V) because we create a dictionary and insert V number of vertices
    def bellmanFord(self, sourceVertex):
        dist = {i : float("inf") for i in self.nodes}
        dist[sourceVertex] = 0
        
        for _ in range(self.V - 1): # O(V)
            for source, destination, weight in self.graph: # O(E)
                if dist[source] != float("inf") and dist[source] + weight < dist[destination]:
                    dist[destination] = dist[source] + weight
                    
        # Check for negative-weight cycle
        for source, destination, weight in self.graph:  # O(E)
            if dist[source] != float("inf") and dist[source] + weight < dist[destination]:
                print("Graph contains negative cycle") 
                return
        
        self.print_solution(dist) 
        
g = Graph(5)
g.addNode("A")         
g.addNode("B")         
g.addNode("C")         
g.addNode("D")         
g.addNode("E")    
g.add_edge("A", "C", 6)      
g.add_edge("A", "D", 6)      
g.add_edge("B", "A", 3)      
g.add_edge("C", "D", 1)      
g.add_edge("D", "C", 2)      
g.add_edge("D", "B", 1)      
g.add_edge("E", "B", 4)      
g.add_edge("E", "D", 2)     

g.bellmanFord("E")
 