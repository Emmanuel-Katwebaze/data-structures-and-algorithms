import math

def countZeroes(customList):
    left = 0
    right = len(customList)-1
    while left <= right:
        middle = math.floor((left + right)/2)
        if customList[middle] == 1:
            left = middle + 1
        else:
            right = middle - 1
    return len(customList) - left