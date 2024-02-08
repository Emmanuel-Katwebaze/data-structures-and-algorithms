# House Robber Problem using Dynamic Programming

# Problem Statement: 
# - Given N number of houses along the street with some amount of money
# - Adjacent houses cannot be stolen
# - Find the maximum amount that can be stolen 
# Houses - 6, 7, 1, 30, 8, 2, 4
# Answer
# - Maximum amount = 41
# - Houses that are stolen : 7, 30, 4

# Top Down Approach
def houseRobberTD(houses, currentIndex, tempDict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            stealFirstHouse = houses[currentIndex] + houseRobberTD(houses, currentIndex + 2, tempDict)
            skipFirstHouse = houseRobberTD(houses, currentIndex + 1, tempDict)
            tempDict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return tempDict[currentIndex]
 
houses = [6, 7, 1, 30, 8, 2, 4]
print("Maximum Amount That Can Be Stolen is ", end="")
print(houseRobberTD(houses, 0, {}))    

# Bottom Up Approach

def houseRobberBU(houses, currentIndex):
    tempArr = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        tempArr[i] = max(houses[i] + tempArr[i+2], tempArr[i+1])
    return tempArr[0]

houses = [6, 7, 1, 30, 8, 2, 4]
print("Maximum Amount That Can Be Stolen is ", end="")
print(houseRobberBU(houses, 0)) 