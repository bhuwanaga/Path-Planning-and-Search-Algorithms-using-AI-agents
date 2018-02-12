import timeit
#Code for DFS

start = timeit.default_timer()
def DFS(x, y, Map):
    if (Map[x][y] == "exit"): # Goal
        return [(x, y)]
    if (Map[x][y] != "path"): # No Path
        return []
    Map[x][y] = "explored" # Visited
    for i in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
        result = DFS(i[0], i[1], Map)
        if len(result) > 0:
            result.append((x, y))
            return result
    return []   # Return Empty list for No Path
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
        if Map[x][y] == "exit": # Goal
            return GetNodes(node)
        if (Map[x][y] != "path"): # No Path
            continue
        Map[x][y] = "explored"  # Visited
        for i in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            queue.append((i[0], i[1], node))
    return []       # Return Empty list for No Path
stop = timeit.default_timer()
print("BFS Execution Time",stop - start)

def GetNodes(node):
    path = []
    while (node != None):
        path.append((node[0], node[1]))
        node = node[2]
    return path

# Predefined Maze using wall and path and exit as goal
def GetMap():
    return[
        ["wall","wall","wall","wall","wall","wall","wall","wall"],
        ["wall","path","wall","wall","wall","wall","wall","wall"],
        ["wall","wall","wall","wall","wall","wall","wall","wall"],
        ["wall","wall","wall","wall","wall","path","wall","wall"],
        ["wall","wall","wall","wall","wall","wall","wall","wall"],
        ["wall","wall","wall","wall","wall","wall","wall","wall"],
        ["wall","wall","wall","wall","path","path","exit","wall"],
        ["wall","wall","wall","wall","wall","wall","wall","wall"]
            ]


#Code for reprentation of solved maze
def GenerateMap(Map, path):
    for x in range(0, len(Map)):
        for y in range(0, len(Map[x])):
            if ((x, y) in path):
                assert Map[x][y] in ("path", "exit")
                print("-", end="")
            elif (Map[x][y] == "wall"):
                print("#", end="")
            elif (Map[x][y] == "exit"):
                print(".", end="")
            else:
                print(' ', end="")
        print()

#Calling
print("unsolved")
GenerateMap(GetMap(), [])
print("\n")
print("solved with DFS")
print("path is ", len(DFS(1, 1, GetMap())), " spots long")
GenerateMap(GetMap(), DFS(1, 1, GetMap()))
print("\n")
print("solved with BFS")
print("path is ", len(BFS(1, 1, GetMap())), " spots long")
GenerateMap(GetMap(), BFS(1, 1, GetMap()))