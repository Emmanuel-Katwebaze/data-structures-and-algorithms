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
    def insert(self, index, data):
        newNode = Node(data)
        if index < 0 or index > self.length:
            return False
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if index == 0:
                newNode.next = self.head
                self.head = newNode
            elif index == 1:
                newNode.next = self.head.next
                self.head.next = newNode
            elif index == self.length:
                self.tail.next = newNode
                newNode.next = None
                self.tail = newNode
            else:
                tempNode = self.head
                inx = 0
                while inx < index-1:
                    tempNode = tempNode.next
                    inx += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
        self.length += 1
        return True