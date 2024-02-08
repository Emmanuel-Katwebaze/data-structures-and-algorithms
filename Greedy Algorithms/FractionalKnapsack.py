# Given a set of items, each with a weight and a value, determine the number of each item to 
# include in a collection so that the total weight is less than or equal to a given limit and the 
# total value is as large as possible.
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

# Time complexity - O(NlogN)
# Space complexity - O(1)        
def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse = True) # O(NlogN)
    usedCapacity = 0
    totalValue = 0
    for item in items:
        if usedCapacity + item.weight <= capacity:
            usedCapacity += item.weight
            totalValue += item.value
        else:
            remainingCapacity = capacity - usedCapacity
            value = item.ratio * remainingCapacity
            usedCapacity += remainingCapacity
            totalValue += value
        
        if usedCapacity == capacity:
            break
        
    print("Total value obtained: " + str(totalValue))
    
item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
customList = [item1, item2, item3] 

knapsackMethod(customList, 50)