import timeit

import numpy as np

#Code for DFS
start = timeit.default_timer()
def DFS(x, y, Map):
    if (Map[x][y] == 2): # Goal
        return [(x, y)]
    if (Map[x][y] != 0): # No Path
        return []
    Map[x][y] = "explored" # Visited
    for i in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
        result = DFS(i[0], i[1], Map)
        if len(result) > 0:
            result.append((x, y))
            return result
    return []  # Return Empty list for No Path
stop = timeit.default_timer()
print("DFS Execution Time:",stop - start)

from collections import deque

#Code for BFS
start = timeit.default_timer()
def BFS(x, y, Map):
    queue = deque([(x, y, None)])
    while len(queue) > 0:
        node = queue.popleft()
        x = node[0]
        y = node[1]
        if Map[x][y] == 2: # Goal
            return GetNodes(node)
        if (Map[x][y] != 0): # No Path
            continue
        Map[x][y] = "explored" # Visited
        for i in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            queue.append((i[0], i[1], node))
    return []  # Return Empty list for No Path
stop = timeit.default_timer()
print("BFS Execution Time",stop - start)

def GetNodes(node):
    path = []
    while (node != None):
        path.append((node[0], node[1]))
        node = node[2]
    return path

#Generating Maze with different probabilities
dim1=6
dim2=6
prob=0.1

def maze(dim1,dim2,prob):
    maz = [[np.random.choice((0,1), p=[1-prob,prob]) for i in range(dim1)] for j in range(dim2)]
    maz[0][0]=0
    maz[dim1-1][dim2-1]=2
    return maz
xmap=maze(dim1,dim2,prob)
print("xmap", np.matrix(xmap))

def GetMap():
    return xmap

#Code for reprentation of solved maze
def GenerateMap(Map, path):
    print(Map)
    for x in range(0, len(Map)):
        for y in range(0, len(Map[x])):
            if ((x, y) in path):
                assert Map[x][y] in (0, 2)
                print("V", end="")
            elif (Map[x][y] == 1):
                print("1", end="")
            elif (Map[x][y] == 2):
                print("2", end="")
            else:
                print('0', end="")
        print()

#Calling

print("solved with DFS")
print("path is ", len(DFS(0, 0, GetMap())), " spots long")
GenerateMap(GetMap(), DFS(0, 0, GetMap()))
print("\n")
print("solved with BFS")
print("path is ", len(BFS(0, 0, GetMap())), " spots long")
GenerateMap(GetMap(), BFS(0, 0, GetMap()))