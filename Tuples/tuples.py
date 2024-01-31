# How to create a Tuple ?
# Time Complexity - O(1)
# Space Complexity - O(n)

newTuple = ('a', 'b', 'c', 'd', 'e')
# or newTuple = 'a', 'b', 'c', 'd', 'e'
newTuple1 = ('a',) # single element tuple must include a comma at the end
newTuple2 = tuple('abcde')

print(newTuple)
print(newTuple1)
print(newTuple2)

# How to access Tuple elements?

print(newTuple[1])
print(newTuple[-1])
print(newTuple[1:3])

# newTuple[0] = 'f' - raises an error because tuples are immutable

# TRAVERSING A TUPLE
# Time Complexity - O(n)
# Space Complexity - O(1)

for i in newTuple:
    print(i)

# OR
for i in range(len(newTuple)):
    print(newTuple[i])
    
# SEARCHING FOR AN ELEMENT 

print('b' in newTuple) # Time Complexity - O(1)

# Time Complexity - O(n)
# Space Complexity - O(1)
def searchTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchTuple(newTuple, 'f'))

# TUPLE OPERATIONS AND FUNCTIONS

myTuple = (1, 4, 3, 2, 5, 2)
myTuple1 = (1, 2, 6, 9, 8, 7)

print(myTuple + myTuple1) # Concatenate two tuples
print(myTuple * 4) # Repeat a tuple n times
print(4 in myTuple)
print(myTuple.count(2)) # counts number of repetitions of a value
print(myTuple.index(4))
print(len(myTuple))
print(max(myTuple))
print(min(myTuple))

print(tuple([1, 2, 3, 4]))

# TUPLES VS LISTS
# 1. List is mutable whereas a tuple is immutable. 
# A tuple does not support reassignment of particular values however we can reassign an entire value.
# We can delete an entire tuple but we cannot delete a single element in a tuple

# 2. Functions that can be used for both lists and tuples: len(), max(), min(), sum(), any(), all(), sorted()

# 3. Methods that can be used for both lists and tuples: count(), index()

# 4. Methods that can NOT be used for tuples: append(), insert(), remove(), pop(), clear(), sort(), reverse()

# 5. Tuples can be stored in Lists. Lists can be stored in Tuples.
# list1 = [(1, 2, 3), (9, 0), (3, 4)]
# tuple1 = ([1, 2, 3], [9, 0], [3, 4])
# tuple2 = ((1, 2, 3), (9, 0), (3, 4))

# We generally use tupes for heterogenous (different) data types and lists for homogenous (similar) data types.
# Iterating through a tuple is faster than with a list since they are immutable.
# Tuples that contain immutable elements can be used as a key for a dictionary unlike a list.
# If you have data that doesn't change, implementing it as a tuple will guarantee that it remains write-protected.

 