# Time complexity - O(1)
# Space complexity - O(n) because of initializing the items list with the number of elements you reeceive as the max size
class Queue:
    def __init__(self, maxSize):
        # initialize the items list with the number of elements you reeceive as the max size
        self.items = maxSize * [None] 
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    # Time complexity - O(1)
    # Space complexity - O(1)
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    # Time complexity - O(1)
    # Space complexity - O(1)
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    # Time complexity - O(1)
    # Space complexity - O(1)
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of the queue"
        
        
    # Time complexity - O(1)
    # Space complexity - O(1)    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            # only one element in the queue
            if self.start == self.top:
                self.start = -1
                self.top = -1
            # if start has reached the end of the list, set it to the beginning
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    # Time complexity - O(1)
    # Space complexity - O(1)    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the queue"
        else:
            return self.items[self.start]
        
    # Time complexity - O(1)
    # Space complexity - O(1)    
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1
        
        

customQueue = Queue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.isFull())

print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())

print(customQueue.delete())
print(customQueue)