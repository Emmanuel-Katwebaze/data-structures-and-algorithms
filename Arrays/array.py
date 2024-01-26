from array import *

# CREATION of an array

arr1 = array('i', [1, 2, 3, 4, 5, 6]) # i stands for integers i.e. creating an array of integers
print(arr1)

arr2 = array('d', [1.3, 1.5, 1.6]) # an array of type of double
print(arr2)

# the complexity of array creation is O(1). In Java when you initialize an empty array 
# and assign values one by one it's O(N).

# INSERTION

# Inserting at the beginning takes O(N) time complexity
# Inserting at the end takes 0(1) time complexity
# Inserting in the middle takes O(N) time complexity
# If an array is full and we want to insert an element into the array we take O(N) time complexity

arr1.insert(6, 7) # insert(index, element)
print(arr1)

arr1.insert(0, 0)
print(arr1)

arr1.insert(2, 9)
print(arr1)

# TRAVERSAL

# Time complexity - O(n)
# Space complexity - O(1) because we don't need an extra space to perform the operation

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)

# ARRAY ELEMENT ACCESSING

# Time complexity - O(1)
# Space complexity - 0(1) we don't need extra space to perform this operation

def accessElement(array, index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])
        
accessElement(arr1, 1)

# SEARCHING FOR A GIVEN VALUE IN THE ARRAY

# If you know where the element is located, use the array indexing access
# If you don't know where it's located, use binary search especially in sorted arrays.
# You could search through each element of the array in order of increasing index basically a linear search.

# If the element is located at the beginning of the array, the time complexity will be O(1)
# Time complexity - O(n)
# Space Complexity - O(1)

def searchInArray(array, value):
    for i in array:
        if i == value:
            # return array.index(value) # Has a time complexity of O(n)
            return True # Has a time complexity of O(1)
    return "The element does not exist in this array"

print(searchInArray(arr1, 3))
print(searchInArray(arr1, 8))

# DELETING AN ELEMENT FROM THE ARRAY

# If you remove the last element from the array the time complexity is O(1)
# else the time complexity is O(n)
# Space complexity - O(1)

arr1.remove(1)
print(arr1)

arr1.remove(7)
print(arr1)

arr1.remove(4)
print(arr1)