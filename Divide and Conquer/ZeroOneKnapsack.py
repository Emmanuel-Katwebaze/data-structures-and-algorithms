# Problem Statement: 
# - Given the weights and profits of N items
# - Find the maximum profit within given capacity of C
# - Items cannot be broken
# Example 1
# Answer Combinations
# - Mango (W:3, P:31) + Apple (W:1,P:26) + Orange (W:2, P:17) = W:6, Profit:74
# - Orange (W:2, P:17) + Banana (W:5,P:72) = W:7, Profit:89
# - Apple (W:1,P:26) + Banana (W:5,P:72) = W:6, Profit:98

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zoKnapsack(items, capacity, currentIndex):
    if capacity <=0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = zoKnapsack(items, capacity, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0))