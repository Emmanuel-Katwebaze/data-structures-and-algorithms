# Question 1 - Missing Number

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def findMissing(list, n):
    sum1 = 100*101/2
    sum2 = sum(list)
    print(sum1-sum2)
    

findMissing(myList, 100)

# Question 2 - Write a program to find all pairs of integers whose sum is equal to a given number
# LeetCode 1 - Two sum
# Pairs have to be distinct

# [2, 6, 3, 9, 11] 9 ------> [6,3]
# Make sure to ask these questions
# - Does array contain only positive or negative numbers?
# - What if the same pair repeats twice, should we print it every time?
# - If the reverse of the pair is acceptable e.g. can we print both (4,1) and (1,4) if the given sum is 5.
# - Do we need to print only distinct pairs? does (3, 3) is a valid pair forgiven sum of 6?
# - How big is the array?

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)
                
myList = [1, 2, 3, 2, 3, 4, 5, 6]
findPairs(myList, 6)

# Question 3 - How to check if an array contains a number in Python

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)
            return True
    return False

print(findNumber(myArray, 8)) # Should return True

# Question 4 - How to find maximum product of two integers in the array where all elements are positive

import numpy as np

myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])

# Time Coplexity - O(n^2 )
def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            # Check if product of current pair is greater than max
            if array[i]*array[j] > maxProduct:
                maxProduct = array[i]*array[j]
                pairs = str(array[i]) + ", " + str(array[j])
    print(pairs)
    print(maxProduct)

findMaxProduct(myArray)

# Question 5 - Is Unique: Implement an algorithm to determine if a list has all unique characters, using python list.

myList = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def isUnique(list):
    a = []
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(isUnique(myList))

# Question 6 - Permutation - two strings have the same characters but in different order

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2: 
        return True
    else:
        return False
    
list1 = [1, 2, 3]
list2 = [1, 3, 2]
print(permutation(list1, list2))

# Question 7 - Given an image represented by an N x N matrix write a method to rotate the image by 90 degrees
import numpy as np

myArray = np.array([[1,2,3],[4,5,6],[7,8, 9]])
print(myArray)

# def rotateImage(matrix):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i,n):
#             temp = matrix[j][i]
#             matrix[j][i] = matrix[i][n-1-j]
#             matrix[i][n-1-j] = temp
            
#     return matrix[::-1] # reverse each row of the matrix

# image = [[1,2,3],[4,5,6],[7,8,9]]
# rotateImage(image)

def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move top to right
            matrix[i][-layer-1] = top
    return matrix

print(rotateMatrix(myArray))
            