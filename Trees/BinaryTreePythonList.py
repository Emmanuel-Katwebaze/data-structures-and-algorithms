# Time complexity - O(1)
# Space complexity - O(n)

class BinaryTree:
    def __init__(self, size):
        self.customLIst = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The binary tree is full"
        self.customLIst[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    def searchNode(self, nodeValue):
        for i in range(len(self.customLIst)):
            if self.customLIst[i] == nodeValue:
                return "Success"
        return "Not Found"
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        print(self.customLIst[index])
        self.preOrderTraversal(index * 2) # O(n/2)
        self.preOrderTraversal((index * 2) + 1) # O(n/2)
        
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(index * 2)
        print(self.customLIst[index])
        self.inOrderTraversal((index * 2) + 1)
        
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal((index * 2) + 1) 
        print(self.customLIst[index])
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customLIst[i])
    
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customLIst[i] == value:
                self.customLIst[i] == self.customLIst[self.lastUsedIndex]
                self.customLIst[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
            
    def deleteBinaryTree(self):
        self.customLIst = None
        return "The binary tree has been successfully deleted"
    
newBinaryTree = BinaryTree(8)

# INSERTION
print("*** INSERTION ***")
# first option - Binary Tree is full
# second option - We have to look for a first vacant place
# Time complexity - O(1)
# Space complexity - O(1)
print(newBinaryTree.insertNode("Drinks"))
print(newBinaryTree.insertNode("Hot"))
print(newBinaryTree.insertNode("Cold"))
print(newBinaryTree.insertNode("Tea"))
print(newBinaryTree.insertNode("Coffee"))

# SEARCHING
# Time complexity - O(n)
# Space complexity - O(1)
print("*** SEARCHING ***")
print(newBinaryTree.searchNode("Tea"))
print(newBinaryTree.searchNode("Hot"))

# PRE ORDER TRAVERSAL
# Time complexity - O(n)
# Space complexity - O(n)
print("*** PRE ORDER TRAVERSAL ***")
newBinaryTree.preOrderTraversal(1)

# IN ORDER TRAVERSAL
# Time complexity - O(n)
# Space complexity - O(n)
print("*** IN ORDER TRAVERSAL ***")
newBinaryTree.inOrderTraversal(1)

# POST ORDER TRAVERSAL
# Time complexity - O(n)
# Space complexity - O(n)
print("*** POST ORDER TRAVERSAL ***")
newBinaryTree.postOrderTraversal(1)

# LEVEL ORDER TRAVERSAL
# Time complexity - O(n)
# Space complexity - O(1)
print("*** LEVEL ORDER TRAVERSAL ***")
newBinaryTree.levelOrderTraversal(1)

# DELETE NODE
# Time complexity - O(n)
# Space complexity - O(1)
print("*** DELETE NODE ***")
print(newBinaryTree.deleteNode("Tea"))
newBinaryTree.levelOrderTraversal(1)

# DELETE BINARY TREE
# Time complexity - O(1)
# Space complexity - O(1)
print("*** DELETE BINARY TREE ***")
print(newBinaryTree.deleteBinaryTree())
newBinaryTree.levelOrderTraversal(1)


