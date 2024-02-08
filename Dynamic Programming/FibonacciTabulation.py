# Fibonacci Series with Tabulation

# Time complexity - O(n)
# Space complexity - O(n)
def fibonacciTab(n):
    tb = [0, 1]
    for i in range(2, n + 1): # starts from index 2 cause first two values of fibonacci are given
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[n - 1]

print(fibonacciTab(6))