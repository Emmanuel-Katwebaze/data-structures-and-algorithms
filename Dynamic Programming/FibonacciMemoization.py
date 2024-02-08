# Fibonacci series with Memoization (Top Down approach)

# Time complexity - O(n)
# Space complexity - O(n)
def fibMemo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n - 2, memo)
    return memo[n]

myDict = {}
print(fibMemo(6, myDict))