def bubbleSort(arr, comparator=None):
    if callable(comparator)==False:
        def comparator(a,b):
            if a < b:
                return -1
            if a > b:
                return 1
            return 0
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if comparator(arr[j], arr[j - 1]) < 0:
                [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]]
            else:
                break
    return arr