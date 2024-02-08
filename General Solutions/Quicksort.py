def pivot (arr, comparator=None, start=0):
    if callable(comparator)==False:
        def comparator(a,b):
            if a < b:
                return -1
            if a > b:
                return 1
            return 0
    pivotIndex = start
    for i in range(start+1,len(arr)):
        if comparator(arr[start], arr[i]) > 0:
            pivotIndex += 1
            [arr[i], arr[pivotIndex]] = [arr[pivotIndex], arr[i]]
    if pivotIndex != start:
        [arr[pivotIndex], arr[start]] = [arr[start], arr[pivotIndex]]
    
    return pivotIndex

def quickSort(arr, comparator=None, start = 0, end=0):
    if start < end:
        pivotIndex = pivot(arr, comparator, start)
        quickSort(arr, comparator, start, pivotIndex - 1)
        quickSort(arr, comparator, pivotIndex + 1, end)
    return arr