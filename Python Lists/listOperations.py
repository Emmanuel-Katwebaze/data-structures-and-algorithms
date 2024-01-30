# ACCESSING / TRAVERSING LISTS

shoppingList = ['Milk', 'Cheese', 'Butter']

print(shoppingList[1])
print(shoppingList[-1])

print('Milk' in shoppingList)
print('Bread' in shoppingList)

# Traversing list

for i in shoppingList:
    print(i)
    
# OR 

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])
    
# Trying to traverse through an empty list won't execute anything

# UPDATE / INSERT
# Time Complexity for accessing/updating - O(1)
# Space Complexity for accessing/updating - O(1)

myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33 # lists are mutable
myList[4] = 55
print(myList)

# Insertion

# insert(), append(), extend()
myList = [1,2,3,4,5,6,7]

# 1. Insert in the beginning of the list
print(myList)
myList.insert(0, 11) # Time Complexity - O(n)
print(myList)

# 2. Insert an element to any given place in the list
myList.insert(4, 15) # Time Complexity - O(n)
print(myList)

# 3. Insert an element to the end of the list
myList.append(55) # Time Complexity & Space Complexity- O(1)
print(myList)

# 4. Inserting another list to the list
newList = [11, 12, 13, 14] # Time Complexity and Space Complexity- O(n)
myList.extend(newList)
print(myList)

# DELETING AN ELEMENT FROM THE LIST

myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2]) # print out first two elements of the list
print(myList[:2]) 
print(myList[1:]) 
print(myList[:]) 

myList[0:2] = ['x', 'y'] # updating multiple elements
print(myList)

myList.pop(1) # delete the second element i.e. y
myList.pop() # delete the last element i.e. f
print(myList.pop(2)) # prints the deleted value

myList = ['a', 'b', 'c', 'd', 'e', 'f']
del myList[1]
print(myList)

del myList[2:4] # second and 3rd index will be deleted
print(myList)

myList.remove('a') # deleting the particular value
print(myList)

# pop function when deleting the last element, Time Complexity - 0(1), 
# in the beginning - Time Complexity 0(n)
# delete - Time Complexity - O(n)
# remove - Time Complexity - O(n)
# Space Complexity for all these methods is O(1)

# SEARCHING FOR AN ELEMENT

myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Time complexity - O(n)
if 20 in myList:
    print(myList.index(20))
else:
    print('THe value does not exist in the list')
    
def searchInList(list, value): # Time complexity - O(n), Space complexity - O(1)
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchInList(myList, 50))

# LIST OPERATIONS / FUNCTIONS
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = a + b
print(c)

d = [0, 4]
d = d * 4
print(d)

a = [0, 1, 2, 3, 4, 5, 6]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a)) # mean

# CHALLENGE
# total = 0
# count = 0
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total / count

# print('Average:', average)

# TRANSFORMED INTO

"""myList = list()
while (True):
    inp = inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    myList.append(value)
average = sum(myList) / len(myList)
    
print('Average:', average)"""

# STRINGS AND LISTS

a = 'spam'
b = list(a)
print(b)

a = 'spam spam spam'
b = a.split()
print(b)

a = 'spam-spam-spam'
delimiter = '-'
b = a.split(delimiter)
print(b)

print(delimiter.join(b))

# PITFALLS AND WAYS TO AVOID THEM

myList = [2, 4, 3, 1, 5, 7]
orig = myList[:]
print(orig)

sorted(myList) # doesn't affect the orig list
print(myList)

myList = myList.sort()
print(myList)

# Similarites between Lists and Arrays
# 1. Both data structures are mutable
# 2. Both can be indexed and iterated through
# 3. They can be both sliced.

# Differences
# Arrays are specially optimized for arithmetic operations

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6])
myList = [1, 2, 3, 4, 5]

print(myArray/2)
# print(myList/2) # generates an error

# In lists the elements data type can be different while in array all elements have to be the same
myArray = np.array([1, 2, 3, 4, 5, 6, 'a'])
myList = [1, 2, 3, 4, 5, 'a']

print(myArray) # become strings
print(myList) # data types remain
 