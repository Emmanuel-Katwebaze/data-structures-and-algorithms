class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next
        
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    # isEmpty
    # Time Complexity - O(1)    
    # Space Complexity - O(1)    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
        
    # push
    # Time Complexity - O(1)    
    # Space Complexity - O(1) 
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        
    # pop
    # Time Complexity - O(1)    
    # Space Complexity - O(1) 
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    # peek
    # Time Complexity - O(1)    
    # Space Complexity - O(1) 
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    # delete
    # Time Complexity - O(1)    
    # Space Complexity - O(1) 
    def delete(self):
        self.LinkedList.head = None
        
    
customStack = Stack()
print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)  
print("---------------------")
customStack.pop()
print(customStack)          
print("---------------------")
print(customStack.peek())          