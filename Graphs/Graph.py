class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    # Time complexity - O(1)  
    # Space complexity - O(1) 
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
    
    # Time complexity - O(1)  
    # Space complexity - O(1) 
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    # Time complexity - O(1)  
    # Space complexity - O(1)  
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    # Time complexity - O(n)  
    # Space complexity - O(1)  
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    

customGraph = Graph()
customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")
customGraph.add_vertex("E")
customGraph.add_edge("A", "B")
customGraph.add_edge("A", "C")
customGraph.add_edge("A", "D")
customGraph.add_edge("B", "C")
customGraph.add_edge("C", "D")
customGraph.print_graph()

print("** REMOVING EDGE **")
customGraph.remove_edge("A", "C")
customGraph.remove_edge("A", "E") # nothing is happening due to exception
customGraph.print_graph()

print("** REMOVING VERTEX **")
customGraph.remove_vertex("D")
customGraph.print_graph()

# GRAPH TRAVERSAL
print("** GRAPH TRAVERSAL **")
class Graph:
    def __init__(self, gdict=None): # gdict - graph dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    # breadth first search 
    # Time complexity - O(V+E)   
    # Space complexity - O(V+E)   
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue: # O(V) where V is the number of vertices
            dequeuedVertex = queue.pop(0)
            print(dequeuedVertex)
            for adjacentVertex in self.gdict[dequeuedVertex]: # O(E) where E is the number of edges
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    # depth first search 
    # Time complexity - O(V+E)  Note: If number of edges are greater than vertices it'll be O(E) but if vertices are greater it'll be O(V)  
    # Space complexity - O(V+E)
    def dfs(self, vertex):
        visited = [vertex]        
        stack = [vertex]
        while stack: # O(V) where V is the number of vertices
            poppedVertex = stack.pop()        
            print(poppedVertex)
            for adjacentVertex in self.gdict[poppedVertex]:  # O(E) where E is the number of edges
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)        
                    

customDict = {"a": ["b", "c"], 
              "b" : ["a", "d", "e"], 
              "c" : ["a", "e"],
              "d" : ["b", "e", "f"],
              "e" : ["d", "f"],
              "f" : ["d", "e"]
              }

graph = Graph(customDict)

print(" *** BREADTH FIRST SEARCH ***")
graph.bfs("a")

print(" *** DEPTH FIRST SEARCH ***")
graph.dfs("a")
            
# TOPOLOGICAL SORT
print(" *** TOPOLOGICAL SORT ***")
from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
        
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
        
    #  if a vertex depends on currentVertex:
    #     Go to that vertex and ---------------- represented by topologicalUtil function
    #     then come back to currentVertex-----|
    # else
    #     Push currentVertex to Stack
    
    # Time complexity - O(E)    
    def topologicalSortUtil(self, v, visited, stack): # basically checks that 
        visited.append(v)
        
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        stack.insert(0, v)
    
    # Time complexity - O(V+E)
    # Space complexity - O(V+E)
    def topologicalSort(self):
        visited = []
        stack = []
        
        for k in list(self.graph): # looping through the vertices in the graph, Time complexity O(E+V)
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
                
        print(stack)

customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

customGraph.topologicalSort()