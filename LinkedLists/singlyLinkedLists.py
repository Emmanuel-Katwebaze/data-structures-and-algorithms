# Process of Creating head and tail - O(1)
# Process of creating a node - O(1)
# Process of assigning a value and next node is O(1)
# Creating the links of head, next and tail is O(1)
# TIME COMPLEXITY For creating a singly linked list is O(1)
# Space complexity is O(1) for creating a new node. If you create more than one node, the space complexity is O(n)

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in LinkedList
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
                    
    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print('The singly linked list does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
                
    # Search for a node in the Singly Linked List
    def searchSSL(self, nodeValue):
        if self.head is None:
            return "The list does not exist"
        else: 
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return 'The value does not exist in this list'
    
    # Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("The SSL does not exist")
        else:
            # deleting the first node
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                # deleting the last node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                # deleting from anywhere
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next    
    
    # Delete entire SSL
    def deleteEntireSSL(self):
        if self.head is None:
            print("The SSL does not exist")
        else: 
            self.head = None
            self.tail = None     
                    
                
                
    
        

singlyLinkedList = SinglyLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

print([node.value for node in singlyLinkedList])



# INSERTION
# Time Complexity at the beginning - O(1), at the end and middle - O(n) 
# Space Complexity - O(1) because we are just creating 2 nodes i.e. newNode and tempNode
singlyLinkedList.insertSLL(5, 1)

print([node.value for node in singlyLinkedList])

singlyLinkedList.insertSLL(3, -1)

print([node.value for node in singlyLinkedList])

singlyLinkedList.insertSLL(0, 0)

print([node.value for node in singlyLinkedList])

# TRAVERSAL
# Time Complexity - O(n)
# Space Complexity - O(1) cause we create one temporary node

singlyLinkedList.traverseSLL()

# SEARCHING
# Time Complexity - O(n)
# Space complexity - O(1)

print(singlyLinkedList.searchSSL(3))
print(singlyLinkedList.searchSSL(31))

# DELETION
# Time complexity - O(n)
# Space complexity - O(1)

print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNode(-1)
print([node.value for node in singlyLinkedList])

# Delete entire SSL
# Time complexity - O(1)
# Space complexity - O(1)

print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteEntireSSL()
print([node.value for node in singlyLinkedList])

