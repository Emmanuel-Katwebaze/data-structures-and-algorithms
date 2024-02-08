class MaxHeap:
    def __init__(self, size):
        self.values = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
    


def heapifyTreeInsert(rootNode, index):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if rootNode.values[index] > rootNode.values[parentIndex]:
            temp = rootNode.values[index]
            rootNode.values[index] = rootNode.values[parentIndex]
            rootNode.values[parentIndex] = temp
    heapifyTreeInsert(rootNode, parentIndex)
    
def insertNode(rootNode, nodeValue):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full"
    rootNode.values[rootNode.heapSize+1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize)

    return "The value has been successfully inserted"


def heapifyTreeExtract(rootNode, index):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    # if there is no child of this node then return
    if rootNode.heapSize < leftIndex:
        return
    # if there is only left child then we check with rootNode and swap
    elif rootNode.heapSize == leftIndex:
        if rootNode.values[index] < rootNode.values[leftIndex]:
                temp = rootNode.values[index]
                rootNode.values[index] = rootNode.values[leftIndex]
                rootNode.values[leftIndex] = temp
        return      
    #  if both children there we find out smallest
    else:       
        #  if parent is greater than smalllest child then swap
        if rootNode.values[leftIndex] > rootNode.values[rightIndex]:
                swapChild = leftIndex
        else:
            swapChild = rightIndex
            if rootNode.values[index] < rootNode.values[swapChild]:
                temp = rootNode.values[index]
                rootNode.values[index] = rootNode.values[swapChild]
                rootNode.values[swapChild] = temp
            
    heapifyTreeExtract(rootNode, swapChild)


def extractMax(rootNode):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.values[1]
        rootNode.values[1] = rootNode.values[rootNode.heapSize]
        rootNode.values[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1)
        return extractedNode