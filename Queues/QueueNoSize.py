# Time complexity - O(1)
# Space complexity - O(1)

class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    # isEmpty
    # Time complexity - O(1)
    # Space complexity - O(1)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    # Enqueue
    # Time complexity - amortized constant O(1) - could reach O(n) or even O(n^2)
    # Space complexity - O(1)
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of the Queue"
    
    
    # Dequeue
    # Time complexity - O(n) - all elements have to shift to the left because you've removed the first element
    # Space complexity - O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items.pop(0) # remove from beginning of the list
        
    # Peek
    # Time complexity - O(1)
    # Space complexity - O(1)
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[0]
    
    # Delete
    # Time complexity - O(1)
    # Space complexity - O(1)
    def delete(self):
        self.items = None
    

customQueue = Queue()
print(customQueue.isEmpty())

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)    
print(customQueue.peek())
    