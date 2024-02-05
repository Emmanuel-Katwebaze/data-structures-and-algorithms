# ensures optimum solution for all pairs shortest path problem

INF = 9999
def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end = " ")
        print(" ")

# Time complexity - O(V^3)        
# Space complexity - O(V^2) because we create a two dimensional list i.e. the distance     
def floydWarshall(nV, G):
    distance = G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                # take the minimum between the direct path or the path through another node
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    
    printSolution(nV, distance)
    
G = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF], 
    [INF, 2, 9, 1],
     ]

floydWarshall(4, G)

# NOTE 
# For all pair shortest path problem, 
# BFS algorithm
# - Time complexity - O(V^3)
# - Space complexity - O(EV)
# Dijsktra's algorithm
# - Time complexity - O(V^3)
# - Space complexity - O(EV)
# Bellman Form algorithm
# - Time complexity - O(EV^2)
# - Space complexity - O(V^2)