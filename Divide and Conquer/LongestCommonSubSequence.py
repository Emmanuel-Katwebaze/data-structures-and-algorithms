# - S1 and S2 are given strings
# - Find the length of the longest subsequence which is common to both strings 
# - Subsequence: a sequence that can be driven from another sequence by deleting some elements 
# without changing the order of them

# Example
# - S1 = “elephant”
# - S2 = “erepat”
# - Output = 5
# - Longest String : “eepat”

def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1 + 1, index2 + 1)
    else:
        op1 = findLCS(s1, s2, index1, index2 + 1)
        op2 = findLCS(s1, s2, index1 + 1, index2)
        return max(op1, op2)
    
print(findLCS("elephant", "erepat", 0, 0))