# - S is a given string
# - Find the longest palindromic subsequence (LPS)
# - Subsequence: a sequence that can be driven from another sequence by deleting some elements 
# without changing the order of them 
# - Palindrome is a string that reads the same backward as well as forward e.g. MADAM
# Example 1
# - S = “ELRMENMET”
# - Output = 5
# - LPS: “EMEME”
# Example 2
# - S = “AMEEWMEA”
# - Output = 6
# - LPS: “AMEEMA”

def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0 
    elif startIndex == endIndex:
        return 1   
    elif s[startIndex] == s[endIndex]:
        return 2 + findLPS(s, startIndex + 1, endIndex)
    else:
        op1 = findLPS(s, startIndex, endIndex - 1)
        op2 = findLPS(s, startIndex + 1, endIndex)
        return max(op1, op2)

print(findLPS("ELRMENMET", 0, 8))