class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    # Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"
    
    # Insertion method of Circular Doubly Linked List
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"
        
    # Traversal of Circular Doubly Linked List
    def traverseCDLL(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if  tempNode == self.tail:
                    break
                tempNode = tempNode.next
        
    # Reverse Traversal of Circular Doubly Linked List
    def reverseTraverseCDLL(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if  tempNode == self.head:
                    break
                tempNode = tempNode.prev
                
    # Search Circular Doubly Linked List
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in the CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                elif tempNode == self.tail:
                    return "The value does not exist in the CDLL"
                tempNode = tempNode.next
    
    # Delete a node from Circular Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("The node has been successfully deleted")
            
    # Delete entire Circular Doubly Linked List
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNodeNext = tempNode.next
                tempNode.next = None
                tempNode = tempNodeNext
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")
            
    # Generated an infinite loop
    # def deleteCDLL(self):
    #     if self.head is None:
    #         print("There is not any element to delete")
    #     else:
    #         self.tail.next = None
    #         tempNode = self.head
    #         while tempNode:
    #             tempNode.prev = None
    #             tempNode = tempNode.next
    #         self.head = None
    #         self.tail = None
    #         print("The CDLL has been successfully deleted")
                
    

# CREATION
# Time complexity - O(1)
# Space complexity - O(1)

circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
print([node.value for node in circularDLL])

# INSERTION
# Time complexity  - O(1) at the beginning and end, O(n) in the middle
# Space complexity - O(1)
circularDLL.insertCDLL(0, 0)
circularDLL.insertCDLL(1, -1)
circularDLL.insertCDLL(2, 2)
print([node.value for node in circularDLL])

# TRAVERSAL
# Time complexity - O(n)
# Space complexity - O(1)
circularDLL.traverseCDLL()

# REVERSE TRAVERSAL
# Time complexity - O(n)
# Space complexity - O(1)
circularDLL.reverseTraverseCDLL()

# SEARCH
# Time complexity - O(n)
# Space complexity - O(1)
print(circularDLL.searchCDLL(5))
print(circularDLL.searchCDLL(50))

# DELETION
# Time complexity - O(1) at the beginning and end, O(n) in the middle
# Space complexity - O(1)

print([node.value for node in circularDLL])
circularDLL.deleteNode(0)
print([node.value for node in circularDLL])
circularDLL.deleteNode(-1)
print([node.value for node in circularDLL])
circularDLL.deleteNode(1)
print([node.value for node in circularDLL])

# DELETE ENTIRE LINKED LIST
# Time complexity - O(n)
# Space complexity - O(1)


circularDLL.deleteCDLL()

print([node.value for node in circularDLL])
