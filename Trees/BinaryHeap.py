# Time complexity - O(1)
# Space complexity - O(n)
class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
    
# Time complexity - O(1)    
# Space complexity - O(1)    
def peekOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]    

# Time complexity - O(1)    
# Space complexity - O(1)   
def sizeOfHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.heapSize 

# Time complexity - O(n)    
# Space complexity - O(1) 
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i])
        
# Time complexity - O(logN)    
# Space complexity - O(logN)     
# A method that adjusts the Binary Heap in the proper format after inserting the new node at the very end 
# basically it adjusts the new node to its correct position in the hierarchy
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType) # O(logN)

# Time complexity - O(logN)    
# Space complexity - O(logN)        
def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The binary heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType) # O(logN)

# Time complexity - O(logN)    
# Space complexity - O(logN)         
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1 
        heapifyTreeExtract(rootNode, 1, heapType) # O(logN)
        return extractNode
    
# Time complexity - O(1)    
# Space complexity - O(1)    
def deleteEntireBH(rootNode):
    rootNode.customList = None
 
    
newBinaryHeap = Heap(5)
print(sizeOfHeap(newBinaryHeap))

insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
levelOrderTraversal(newBinaryHeap)

print("*** EXTRACTION ***")
print(extractNode(newBinaryHeap, "Max"))
levelOrderTraversal(newBinaryHeap)

print("*** DELETE ENTIRE HEAP ***")
deleteEntireBH(newBinaryHeap)
levelOrderTraversal(newBinaryHeap)