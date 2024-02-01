# Time complexity - O(1)
# Space complexity - O(1)

class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    # pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
        
    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]
    
    # delete
    def delete(self):
        self.list = None

# isEmpty
# Time complexity - O(1)
# Space complexity - O(1)
customStack = Stack()
print(customStack.isEmpty())


# push
# Time complexity - amortized constant O(1) tends towards O(n) the more the number of values grows
# Space compexity - O(1)
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

# pop
# Time complexity - O(1) just removing one element from the list
# Space complexity - O(1)
print(customStack.pop())
print("Stack items are:")
print(customStack)

# peek
print("Peek")
# Time complexity - O(1) accessing any given element of a list
# Space complexity - O(1)
print(customStack.peek())
print("Stack items are:")
print(customStack)

# delete
# Time complexity - O(1) 
# Space complexity - O(1)
print(customStack.delete())