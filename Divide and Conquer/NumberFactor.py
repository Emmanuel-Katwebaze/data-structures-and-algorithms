# Given N, find the number of ways to express N as a sum of 1, 3 and 4. 
# Example 1
# - N = 4
# - Number of ways = 4
# - Explanation : There are 4 ways we can express N. {4},{1,3},{3,1},{1,1,1,1}
# Example 2
# - N = 5
# - Number of ways = 6
# - Explanation : There are 6 ways we can express N. {4,1},{1,4},{1,3,1},{3,1,1},{1,1,3},{1,1,1,1,1}

def numberFactor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        subProb1 = numberFactor(n-1)
        subProb2 = numberFactor(n-3)
        subProb3 = numberFactor(n-4)
        return subProb1 + subProb2 + subProb3
    
print(numberFactor(5)) # returns 6