class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL has been created Successfully"
    
    # Insertion Method in Doubly Linked List
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
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
                
    # Traversal Method in Doubly Linked List
    def traverselDLL(self): 
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                
    # Reverse Traversal Method in Doubly Linked List
    def reverseTraverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
                
    # Search Method in Doubly Linked List
    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is not any element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value 
                tempNode = tempNode.next
            return "The node does not exist in this list"
        
    # Delete a node from Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any element in the DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode
            print("The node has been successfully deleted")
            
    # Delet entire Doubly Linked List
    def deleteDLL(self):
        if self.head is None:
            print("There is not any node in DLL")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")
                
                
    
    

# CREATION
# Time complexity - O(1)
# Space complexity - O(1)
    
doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])

# INSERTION
# Time complexity - O(1) at the beginning and end , O(n) in the middle
# Space complexity - O(1)

doublyLL.insertNode(0, 0)
doublyLL.insertNode(1, 1)
doublyLL.insertNode(2, -1)
doublyLL.insertNode(6, 2)

print([node.value for node in doublyLL])

# FORWARD TRAVERSAL
# Time complexity - O(n)
# Space complexity - O(1)

doublyLL.traverselDLL()

# REVERSE TRAVERSAL
# Time complexity - O(n)
# Space complexity - O(1)

doublyLL.reverseTraverseDLL()

# SEARCHING
# Time complexity - O(n)
# Space complexity - O(1)

print(doublyLL.searchDLL(6))
print(doublyLL.searchDLL(60))

# DELETION
# Time complexity - O(1) at the beginning and end, O(n) for the middle
# Space complexity - O(1)

print([node.value for node in doublyLL])

doublyLL.deleteNode(0)
print([node.value for node in doublyLL])

doublyLL.deleteNode(-1)
print([node.value for node in doublyLL])

doublyLL.deleteNode(1) # won't work for doublyLL.deleteNode(2)
print([node.value for node in doublyLL])

# Delete an entire doubly linked list
# Time complexity - O(n)
# Time complexity - O(1)

doublyLL.deleteDLL()
print([node.value for node in doublyLL])