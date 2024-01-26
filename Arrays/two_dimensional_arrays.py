# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np

# Time Complexity - O(1)
# And if you create an empty array and assign values one by one then it's O(n)
# Space complexity - O(mn) because you need m number of rows and n number of columns

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# INSERTION
# Time Complexity - O(mn) while when inserting at the end, time complexity is O(1)

# Inserting a new column to the 2D array on column 1
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)
print(newTwoDArray)

# Inserting a new row to the 2D array on row 1
newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

# Inserting at the end of a 2D array
newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]])
print(newTwoDArray)

# ACCESSING ELEMENTS IN 2D ARRAY
# array_name[row_index][column_index]
# Time Complexity - O(1)
# Space complexity - O(1)

def accessElements(array, rowIndex, columnIndex):
    # len(array) - returns number of rows and len(array[0]) returns the number of columns
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print("Index out of range")
    else:
        print(array[rowIndex][columnIndex])
        
accessElements(twoDArray, 1, 2)

# TRAVERSING 
# If number of rows is equal to number of columns, time complexity is O(n^2)
# else Time Complexity - O(mn)
# Space Complexity - O(1)

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
            

traverseTDArray(twoDArray)

# SEARCHING
# Linear search - Time Complexity - O(mn) when number of rows is not equal to number of columns
# O(n^2) - when number of rows is equal to number of rows
# Space complexity - O(1)

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index ' + str(i)+" "+str(j)
    return 'The element is not found'


print(searchTDArray(twoDArray, 14))

# DELETION
# Time complexity - O(mn) - unequal rows and columns
# Time complexity - O(n^2) or O(m^2)- quadratic
# Space complexity - O(1)

newTDArray = np.delete(twoDArray, 0, axis=0)
print(newTDArray)





        
