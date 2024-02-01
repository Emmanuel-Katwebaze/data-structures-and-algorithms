from LinkedList import LinkedList


# 1. Write code to remove duplicates from an unsorted linked list
# Time complexity - O(n)
# Space complexity - O(n) because we are creating a new set and adding the elements into it

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll

# in case they saw we cannot use a temporary buffer
# Time complexity - O(n^2)
# Space complexity - O(1) 
def removeDups1(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
            currentNode = currentNode.next
        return ll.head

print("*** QUESTION ONE ***")    
# case one    
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups(customLL)
print(customLL)

    
# case two
customLL2 = LinkedList()
customLL2.generate(10, 0, 99)
print(customLL2)
removeDups(customLL2)
print(customLL2)

print("*** QUESTION TWO ***")  
# 2. Implement an algorithm to find the nth to last element of a singly linked list
# Iteration is the most optimal solution but less straightforward
# uses two pointers.

# Time complexity - O(n)
# Space complexity - O(1)

def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head
    
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
        
    while pointer2: # means until pointer 2 reaches the last node
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))

print("*** QUESTION THREE ***")  
# 3. Write code to partition a linked list around a value x, such that all nodes less than x
# come before all nodes greater than or equal to x.
# Note: The values don't have to be in order

# Time complexity - O(n)
# Space complexity - O(1)

def partition(ll, x):
    currentNode = ll.head
    ll.tail = ll.head
    
    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < x:
            currentNode.next = ll.head
            ll.head = currentNode
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
        currentNode = nextNode
    
    # in case if all elements are less than the next value
    if ll.tail.next is not None: 
        ll.tail.next = None
        
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
partition(customLL, 30)
print(customLL)

print("*** QUESTION FOUR ***") 
# 4. You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that 1's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.

# Time complexity - O(n)
# Space complexity - O(n)

def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()
    
    # 7, 1, 6
    # 5, 9, 2
    
    # 0, 7, 12 carry - 1 | 1, 2, 11 carry - 1 | 1, 7, 9 carry - 0 | n1 and n2 become None hence stop
    # 2 -> 1 -> 9
    
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    
    return ll

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)

print(sumList(llA, llB))

print("*** QUESTION FIVE ***") 
# 5. Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value. That is, if the kth node of the first 
# linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

# Time complexity - O(A + B) based off the number of nodes in the two lists
# Space complexity - O(1)

from LinkedList import Node

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)
    
    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA
    
    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head
    
    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
        
    return longerNode

# Helper addtion method
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode
    
llA = LinkedList()
llA.generate(3, 0, 10)

llB = LinkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))