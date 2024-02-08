import math

def findRotatedIndex(arr, num):
    left = 0
    right = len(arr) - 1
    if right>0 and arr[left] >= arr[right]:
        middle = math.floor((left + right) / 2)
        while (arr[middle] <= arr[middle + 1]):
            if arr[left] <= arr[middle]:
                left = middle + 1
            else:
                right = middle - 1
            middle = math.floor((left + right) / 2)
            if middle+1 > len(arr)-1:
                break
        

        if (num >= arr[0] and num <= arr[middle]):
            left = 0
            right = middle
        else:
            left = middle + 1
            right = len(arr) - 1
    
    while (left <= right):
        middle = math.floor((left + right) / 2)
        if (num == arr[middle]):
            return middle
        if (num > arr[middle]):
            left = middle + 1
        else:
            right = middle - 1
    return -1
        