# BUBBLE SORT
print("*** BUBBLE SORT ***")
# Time complexity - O(n^2)
# Space complexity - O(1)
def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j] # uses a tuple swapping technique
                
                # Using a temporary variable for swapping
                # temp = customList[j]
                # customList[j] = customList[j+1]
                # customList[j+1] = temp

    print(customList)
    
list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
bubbleSort(list)

# When to use Bubble Sort?
# - When the input is already sorted
# - Space is a concern
# - Easy to implement
# When to avoid Bubble Sort?
# -Average time complexity is poor

# SELECTION SORT
# Time complexity - O(n^2)
# Space complexity - O(1)
print("*** SELECTION SORT ***")
def selectionSort(customList):
    for i in range(len(customList) - 1):
        min_index = i
        for j in range(i + 1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)
    
list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
selectionSort(list)

# When to use Selection Sort?
# - When we have insufficient memory 
# - Easy to implement
# When to avoid Selection Sort?
# - When time is a concern

# INSERTION SORT
# Time complexity - O(n^2)
# Space complexity - O(1)
print("*** INSERTION SORT ***")
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    print(customList)

list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
insertionSort(list)

# When to use Insertion Sort?
# - When we have insufficient memory 
# - Easy to implement
# - When we have continuous inflow of numbers and we want to keep 
# them sorted
# When to avoid Insertion Sort?
# - When time is a concern

# BUCKET SORT
# Time complexity - O(NlogN) - when using quick sort, O(n^2) when using bubble sort, insertion sort or selection sort
# Space complexity - O(n)
print("*** BUCKET SORT ***")

import math
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    for i in range(numberOfBuckets):
        arr.append([])
    # Distribute elements into buckets
    for j in customList:
        index_b = math.ceil(j*numberOfBuckets/maxValue)
        arr[index_b - 1].append(j)
        
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(bucketSort(list))

# When to use Bucket Sort?
# - When input uniformly distributed over range
# 1,2,4,5,3,8,7,9  not 1,2,4,91,93,95
# When to avoid Bucket Sort?
# - When space is a concern

# MERGE SORT
print("*** MERGE SORT ***")

# Time complexity of merge function - O(n)
def merge(customList, l, m, r): # l-first index, m- middle, r - last index
    n1 = m - l + 1 # number of elements in first sub array
    n2 = r - m # number of elements in second sub array
    
    L = [0] * (n1)
    R = [0] * (n2)
    
    # copying elements to left sub array
    for i in range(0, n1):
        L[i] = customList[l+i]
    
    # copying elements to right sub array    
    for j in range(0, n2):
        R[j] = customList[m+1+j]
        
    # Merge the smaller arrays
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    
    # Merge to the main list
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j < n1:
        customList[k] = R[j]
        j += 1
        k += 1

# Time complexity - O(NlogN)
# Space complexity - O(n)        
def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r-1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)
    return customList

list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(mergeSort(list, 0, 8))

# When to use Merge Sort?
# - When you need stable sort
# - When average expected time is O(NlogN)

# When to avoid Merge Sort?
# - When space is a concern

# QUICK SORT
print("*** QUICK SORT ***")

# Time complexity - O(n)
# Space complexity - O(1)
def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    # We take the right most number as a pivot and place all numbers that are less than 
    # the pivot on the left and all elements that are greater than the pivot on the right.
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    # replace the value which is bigger than the pivot value by the pivot value
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)

# Time complexity - O(NlogN)
# Space complexity - O(N)
def quickSort(customList, low, high):
    if low < high:
        partition_index = partition(customList, low, high)
        quickSort(customList, low, partition_index-1)
        quickSort(customList, partition_index+1, high)

list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
quickSort(list, 0, 8)
print(list)

# When to use Quick Sort?
# - When you need stable sort
# - When average expected time is O(NlogN)
# When to avoid Quick Sort?
# - When space is a concern

# HEAP SORT
print("*** HEAP SORT ***")

def heapify(customList, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l
        
    if r < n and customList[r] < customList[smallest]:
        smallest = r
    
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)

# Time complexity - O(NlogN)
# Space complexity - O(1)        
def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2) - 1, -1, -1):
        heapify(customList, n, i)
    
    for i in range(n-1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    
    customList.reverse() # places the elements in ascending order since they come in descending order
    
list = [2, 1, 7, 6, 5, 3, 4, 9, 8]
heapSort(list)
print(list)
