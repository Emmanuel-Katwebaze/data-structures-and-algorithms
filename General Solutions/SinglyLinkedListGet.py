class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.next
        return currentNode