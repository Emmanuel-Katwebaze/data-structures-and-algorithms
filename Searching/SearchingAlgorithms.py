# Linear Search
# Time complexity - O(n)
# Space complexity - O(1)
def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

list = [20, 40, 30, 50, 90]
print(linearSearch(list, 50))
print(linearSearch(list, 100))

print(" *** BINARY SEARCH ***")
# Binary Search
# Time complexity - O(logN)
# Space complexity - O(1)
# It takes log base 2 of N steps to find an element in the worst case from an array of N elements
import math
def binarySearch(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start+end)/2)
    # print(start, middle, end)
    # start <= end makes sure we don't enter an infinite loop in case we're searching for something that doesn't exist
    # and the start pointer may end up passing the end
    while not(array[middle] == value) and start<=end: 
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end)/2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    return -1
    
customArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(customArray, 15))
print(binarySearch(customArray, 155))