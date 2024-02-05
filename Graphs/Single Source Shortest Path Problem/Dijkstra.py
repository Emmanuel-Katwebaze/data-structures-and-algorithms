# Used for single source shortest path problem and all pairs shortest path problem
# Dijkstra SSSPP - Finding the path with the minimum sum of the edge weights
# APSPP - involves running SSSPP for all vertices

import heapq # smallest of each element is popped

class Edge:
    def __init__(self, weight, start_vertex, target):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target
        
class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        # previous node to the current node
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float('inf')
    
    def __lt__(self, other_node):  # lt - less than to support comparison properties eg Node("A") < Node("B")
        return self.min_distance < other_node.min_distance
    
    # create edge between current node and destination vertex
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)
    
# Dijkstra's algorithm
# Time complexity - O(V^2)
# Space complexity - O(V)
class Dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        # insert the element into the heap and order is adjusted to maintain the heap DS
        # heapq transforms list into a heap
        heapq.heappush(self.heap, start_vertex) 
        while self.heap:
            # pop element with the lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider the neighbors
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update the heap
                    heapq.heappush(self.heap, target)
                    # [F-19, F-17]
            actual_vertex.visited = True
    
    def get_shortest_path(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor
    
# Step 1 - create nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")
                
# Step 2 - create edges
nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)

        
