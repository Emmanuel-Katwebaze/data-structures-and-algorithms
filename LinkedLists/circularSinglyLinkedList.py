class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
            
    # Creation of circular singly linked list
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
    # Insertion of a node in circular singly linked list
    
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next =newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"
    
    # Traversal of a node in circular singly linked list
    def traverseCSLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
                
    # Searching for a node in circular singly linked list
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CSLL"
                
    # Delete a node from circular singly linked list
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node in CSLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:                        
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
    # Delete entire circular singly linked list
    def deletEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
    

# CREATION
# Time Complexity - O(1)
# Space complexity = O(1)

circularSinglyLinkedList = CircularSinglyLinkedList() 
circularSinglyLinkedList.createCSLL(1)

print([node.value for node in circularSinglyLinkedList])

# INSERTION
# Time complexity - O(1) when inserting at the beginning and end and O(n) when inserting in the middle
# Space complexity - O(1)

print([node.value for node in circularSinglyLinkedList])

circularSinglyLinkedList.insertCSLL(0, 0)

circularSinglyLinkedList.insertCSLL(2, -1)

circularSinglyLinkedList.insertCSLL(3, -1)

circularSinglyLinkedList.insertCSLL(2, 2)

print([node.value for node in circularSinglyLinkedList])

# TRAVERSING
# Time complexity - O(n)
# Space complexity - O(1)

circularSinglyLinkedList.traverseCSLL()

# SEARCHING
# Time complexity - O(n)
# Space complexity - O(1)

print(circularSinglyLinkedList.searchCSLL(3))
print(circularSinglyLinkedList.searchCSLL(23))

# DELETION
# Time complexity - O(1) at the beginning, O(n) from the middle and end
# Space complexity - O(1)

print([node.value for node in circularSinglyLinkedList])
circularSinglyLinkedList.deleteNode(0)
print([node.value for node in circularSinglyLinkedList])
circularSinglyLinkedList.deleteNode(-1)
print([node.value for node in circularSinglyLinkedList])
circularSinglyLinkedList.deleteNode(2)
print([node.value for node in circularSinglyLinkedList])

# Delete entire circular singly linked list
# Time complexity - O(1) 
# Space complexity - O(1)

circularSinglyLinkedList.deletEntireCSLL()
print([node.value for node in circularSinglyLinkedList])

