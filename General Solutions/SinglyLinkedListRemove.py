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
        
    def remove(self, index):
        
        if index < 0 or index >= self.length:
            return None
        if self.head is None:
            return None
        else:
            self.length -= 1
            result = self.head
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                return result
            else:
                tempNode = self.head
                indx = 0
                while indx < index - 1:
                    tempNode = tempNode.next
                    indx += 1
                result = tempNode.next
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                return result