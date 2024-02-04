class Graph:
    def __init__(self, gdict=None): # gdict - graph dictionary
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    # Time complexity - O(E) not O(E+V) because here we are only visiting the 
    # connected vertices and if we have isolated vertices we won't visit them
    # making number of edges greater than number of vertices
    # Space complexity - O(E)
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue: # O(V)
            path = queue.pop(0)
            node = path[-1]            
            if node == end:
                return path            
            for adjacent in self.gdict.get(node, []): # O(E)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                
customDict = {"a" : ["b", "c"], 
              "b" : ["d", "g"], 
              "c" : ["d", "e"], 
              "d" : ["f"], 
              "e" : ["f"], 
              "g" : ["f"]
              }
g = Graph(customDict)
print(g.bfs("a", "f"))