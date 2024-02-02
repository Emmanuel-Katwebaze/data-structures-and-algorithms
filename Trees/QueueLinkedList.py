 
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

# Time complexity - O(1)            
# Space complexity - O(1)            
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    # Time complexity - O(1)            
    # Space complexity - O(1) 
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
            
    # Time complexity - O(1)            
    # Space complexity - O(1) 
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    # Time complexity - O(1)            
    # Space complexity - O(1) 
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    # Time complexity - O(1)            
    # Space complexity - O(1)     
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
        
    # Time complexity - O(1)            
    # Space complexity - O(1) 
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
        
            