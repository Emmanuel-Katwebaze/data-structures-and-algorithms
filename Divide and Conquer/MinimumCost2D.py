# - 2D Matrix is given
# - Each cell has a cost associated with it for accessing
# - We need to start from (0.0) cell and go till (n-1,n-1) cell
# - We can go only to right or down cell from current cell
# - Find the way in which the cost is minimum

def findMinCost(twoDArray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoDArray[0][0]
    else:
        op1 = findMinCost(twoDArray, row - 1, col)
        op2 = findMinCost(twoDArray, row, col - 1)
        return twoDArray[row][col] + min(op1, op2)
    
TwoDList = [[4,7,8,6,4],
           [6,7,3,9,2],
           [3,8,1,2,4],
           [7,1,7,3,7],
           [2,9,8,9,3]
           ]

print(findMinCost(TwoDList, 4,4))