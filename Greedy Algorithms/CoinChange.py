# You are given coins of different denominations and total amount of money. Find the minimum 
# number of coins that you need yo make up the given amount.
# Infinite supply of denominations : {1,2,5,10,20,50,100,1000}
# Example 1
# Total amount : 7
# Answer: 2 —> 50 + 20 = 70

# Time complexity - O(n)
# Space complexity - O(1)
def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    lastIndex = len(coins) - 1
    while True:
        coinValue = coins[lastIndex]
        if N >= coinValue:
            print(coinValue) # if you create a custom list here and add the values, space complexity will be O(n)
            N = N - coinValue
        if N < coinValue:
            lastIndex -= 1
        
        if N == 0:
            break

coins = [1, 2, 5, 20, 50, 100]
coinChange(201, coins)