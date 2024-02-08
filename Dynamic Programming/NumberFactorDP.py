# Number Factor Problem using Dynamic Programming

# Given N, find the number of ways to express N as a sum of 1, 3 and 4. 
# Example 1
# - N = 4
# - Number of ways = 4
# - Explanation : There are 4 ways we can express N. {4},{1,3},{3,1},{1,1,1,1}
# Example 2
# - N = 5
# - Number of ways = 6
# - Explanation : There are 6 ways we can express N. {4,1},{1,4},{1,3,1},{3,1,1},{1,1,3},{1,1,1,1,1}

# Top Down Approach
def numberFactorTD(n, tempDict):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempDict:
            subP1 = numberFactorTD(n - 1, tempDict)
            subP2 = numberFactorTD(n - 3, tempDict)
            subP3 = numberFactorTD(n - 4, tempDict)
            tempDict[n] = subP1 + subP2 + subP3
        return tempDict[n]

print(numberFactorTD(5, {}))

# Bottom Up Approach
def numberFactorBU(n):
    tempArr = [1, 1, 1, 2]
    for i in range(4, n + 1):
        tempArr.append(tempArr[i - 1] + tempArr[i - 3] + tempArr[i - 4])
    return tempArr[n]
    
print(numberFactorBU(5))