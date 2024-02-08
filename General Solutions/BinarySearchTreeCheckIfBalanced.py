class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST:
    def __init__(self):
        self.root = Node(None)

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = Node(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = Node(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"

def getHeight(rooNode):
    if rooNode == None:
        return 0
    return max(getHeight(rooNode.leftChild), getHeight(rooNode.rightChild)) + 1


def isBalanced(rooNode):
    if rooNode == None:
        return True
    return abs(getHeight(rooNode.leftChild)-getHeight(rooNode.rightChild)) <= 1 