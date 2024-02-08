class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def enqueue(self, data):
        newNode = Node(data)
        if self.first == None:
            self.first = newNode
        else:
            self.last.next = newNode
        
        self.last = newNode
        self.size += 1

        return self.size