
# Time complexity - O(1) 
# Space complexity - O(1)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBinaryTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBinaryTree.leftChild = leftChild
newBinaryTree.rightChild = rightChild

print(" *** PREORDER TRAVERSAL ***")
# Pre-order Traversal
# Time complexity - O(n)
# Space complexity - O(n) because we're using stack memory
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild) # O(n/2)
    preOrderTraversal(rootNode.rightChild) # O(n/2)
    
preOrderTraversal(newBinaryTree)

print(" *** INORDER TRAVERSAL ***")
# In-order Traversal
# Time complexity - O(n)
# Space complexity - O(n) because we're using stack memory
def inOrderTraversal(rootNode):
    if not rootNode:
        return    
    inOrderTraversal(rootNode.leftChild) # O(n/2)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild) # O(n/2)
    
inOrderTraversal(newBinaryTree)

print(" *** POST ORDER TRAVERSAL ***")
# Post-order Traversal
# Time complexity - O(n)
# Space complexity - O(n) because we're using stack memory
def postOrderTraversal(rootNode):
    if not rootNode:
        return        
    postOrderTraversal(rootNode.leftChild) # O(n/2)
    postOrderTraversal(rootNode.rightChild) # O(n/2)
    print(rootNode.data)
    
postOrderTraversal(newBinaryTree)

print(" *** LEVEL ORDER TRAVERSAL ***")
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
    
levelOrderTraversal(newBinaryTree)

# SEARCHING 
# Use level order traversal because it uses a queue and a queue is more efficient than a stack
# Time complexity - O(n)
# Space complexity - O(n)

print(" *** SEARCHING ***")
def searchBinaryTree(rootNode, nodeValue):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found"
    
print(searchBinaryTree(newBinaryTree, "Tea"))

# INSERTION
# first case - Root node is blank
# second case - tree exists and we have to look for a first vacant place
# Time complexity - O(n)
# Space complexity - O(n)

print(" *** INSERTION ***")
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"
            

newNode = TreeNode("Cola")
print(insertNodeBT(newBinaryTree, newNode))
levelOrderTraversal(newBinaryTree)

# DELETION
# first case - value does not exist
# second case - value exists 
# Have to first find the deepest node, make the value you want to delete the deepest node,
# then delete the deepest node

print(" *** DELETION ***")

def getDeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode
    

# deepestNode = getDeepestNode(newBinaryTree)
# print(deepestNode.data)

def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is deepestNode:
                root.value = None
                return
            elif root.value.rightChild:
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            elif root.value.leftChild:
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
                    
# deepestNode = getDeepestNode(newBinaryTree)
# deleteDeepestNode(newBinaryTree, newNode)
# levelOrderTraversal(newBinaryTree)

# *** Main Function ***
# Time complexity - O(n)
# Space complexity - O(n)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                deepestNode = getDeepestNode(rootNode)
                root.value.data = deepestNode.data
                deleteDeepestNode(rootNode, deepestNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed to delete"
    

print(deleteNodeBT(newBinaryTree, "Tea"))
levelOrderTraversal(newBinaryTree)

print(" *** DELETE ENTIRE BINARY TREE ***")
# Time complexity - O(1)
# Space complexity - O(1)

def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The binary tree has been successfully deleted"

print(deleteBinaryTree(newBinaryTree))
levelOrderTraversal(newBinaryTree)