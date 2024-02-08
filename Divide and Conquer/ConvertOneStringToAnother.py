# - S1 and S2 are given strings
# - Convert S2 to S1 using delete, insert or replace operations
# - Find the minimum count of edit operations
# Example 1
# - S1 = “catch”
# - S2 = “carch”
# - Output = 1
# - Explanation : Replace “r” with “t”
# Example 2
# - S1 = “table”
# - S2 = “tbres”
# - Output = 3
# - Explanation : Insert “a” to second position, replace “r” with “l” and delete “s”

def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1 + 1, index2 + 1)
    else:
        delete = 1 + findMinOperation(s1, s2, index1, index2 + 1)
        insert = 1 + findMinOperation(s1, s2, index1 + 1, index2)
        replace = 1 + findMinOperation(s1, s2, index1 + 1, index2 + 1)
        return min(delete, insert, replace)

print(findMinOperation("catch", "carch", 0, 0))
print(findMinOperation("table", "tbres", 0, 0))