# Time complexity - O(n)
# Space complexity - O(n)
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    
    # Time complexity - O(1)    
    # Space complexity - O(1)    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    
    # Time complexity - O(1)    
    # Space complexity - O(1) 
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
            

# vertices = ["A", "B", "C", "D", "E"]

# ds = DisjointSet(vertices)
# print(ds.find("A"))
# ds.union("A", "B")
# print(ds.find("B"))
# ds.union("A", "C")
# print(ds.find("A"))