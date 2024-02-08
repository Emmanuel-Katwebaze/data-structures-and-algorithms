# Problem Statement: 
# - Given N number of houses along the street with some amount of money
# - Adjacent houses cannot be stolen
# - Find the maximum amount that can be stolen 
# Houses - 6, 7, 1, 30, 8, 2, 4
# Answer
# - Maximum amount = 41
# - Houses that are stolen : 7, 30, 4

def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        skipFirstHouse = houseRobber(houses, currentIndex + 1)
        return max(stealFirstHouse, skipFirstHouse)

houses = [6, 7, 1, 30, 8, 2, 4]
print("Maximum Amount That Can Be Stolen is ", end="")
print(houseRobber(houses, 0))