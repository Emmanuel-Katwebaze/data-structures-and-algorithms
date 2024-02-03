# Time complexity - O(1)
# Space complexity - O(1)
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        

# Time complexity - O(logN)
# Space complexity - O(logN)
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTree(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTree(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue) 
    return "The node has been successfully inserted"

# Time complexity - O(n)
# Space complexity - O(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# Time complexity - O(n)
# Space complexity - O(n)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# Time complexity - O(n)
# Space complexity - O(n)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
import QueueLinkedList as queue
    
# Level-order Traversal
# Time complexity - O(n)
# Space complexity - O(n) because we're using a custom queue DS and inserting all elements of the tree i the queue
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()       
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
            
# Time complexity - O(logN)
# Space complexity - O(logN)
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)
    
def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

# Time complexity - O(logN)
# Space complexity - O(logN)
def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        # Deleting a node which has only one child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        # Deleting a node which has two children
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode 

# Time complexity - O(1)
# Space complexity - O(1)
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The binary search tree has been successfully deleted"
    
    
            
print(" *** INSERT NODE ***")        
newBinarySearchTree = BinarySearchTree(None)
print(insertNode(newBinarySearchTree, 70))
print(insertNode(newBinarySearchTree, 60))
print(newBinarySearchTree.data)
print(newBinarySearchTree.leftChild.data)
            
print(" *** PRE ORDER TRAVERSAL ***")        
newBinarySearchTree = BinarySearchTree(None)
insertNode(newBinarySearchTree, 70)
insertNode(newBinarySearchTree, 50)
insertNode(newBinarySearchTree, 90)
insertNode(newBinarySearchTree, 30)
insertNode(newBinarySearchTree, 60)
insertNode(newBinarySearchTree, 80)
insertNode(newBinarySearchTree, 100)
insertNode(newBinarySearchTree, 20)
insertNode(newBinarySearchTree, 40)
preOrderTraversal(newBinarySearchTree)

print(" *** IN ORDER TRAVERSAL ***") 
inOrderTraversal(newBinarySearchTree)

print(" *** POST ORDER TRAVERSAL ***") 
postOrderTraversal(newBinarySearchTree)

print(" *** LEVEL ORDER TRAVERSAL ***") 
levelOrderTraversal(newBinarySearchTree)

print(" *** SEARCHING ***") 
searchNode(newBinarySearchTree, 60)

print(" *** DELETE NODE ***") 
deleteNode(newBinarySearchTree, 20)
levelOrderTraversal(newBinarySearchTree)

print(" *** DELETE BINARY SEARCH TREE ***") 
print(deleteBST(newBinarySearchTree))
levelOrderTraversal(newBinarySearchTree)

# NOTE: In case the Binary Search Tree is imbalanced, the Time complexities for 
# insertion, traversing, searching and deletion can reach O(n)