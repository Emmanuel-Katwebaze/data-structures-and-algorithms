# Time complexity - O(1)
# Space complexity - O(1)
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1
        
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

def getHeight(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.height

# Time complexity - O(1)
# Space complexity - O(1)
def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# Time complexity - O(1)
# Space complexity - O(1)
def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# Time complexity - O(1)
# Space complexity - O(1)
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

# Time complexity - O(logN)
# Space complexity - O(logN)
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
       rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue) 
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    
    # if the left child's height is greater than the right child's height and the difference between them is more than one
    # and you are inserting this node value on the left child of the root node, so this becomes left left
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    # left right condition
    if balance > 1 and nodeValue < rootNode.rightChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # right right condition
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    # right left condition
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

# Time complexity - O(logN)
# Space complexity - O(logN)
def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
        # rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    
    # Left left condition
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    # Right right condition
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    # Left Right condition
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # Right left condition
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = leftRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
# Time complexity - O(1)
# Space complexity - O(1)
def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None    
    rootNode.rightChild = None 
    return "The AVL has been successfully deleted"   



print("*** INSERTION ***")        
newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
levelOrderTraversal(newAVL)

print("*** DELETION ***")   
deleteNode(newAVL, 15)
levelOrderTraversal(newAVL)

print("*** DELETE ENTIRE AVL ***")   
deleteAVL(newAVL)
levelOrderTraversal(newAVL)
