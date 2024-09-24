isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]
n = len(isConnected)

# generate graph
graph = {}
for i in range(n):
    graph[i] = []
    for j in range(n):
        if isConnected[i][j] == 1 and i != j:
            graph[i].append(j)
print(graph)

# generate its dfs
def dfs_traversal(vertice,visited):
    if vertice not in visited:
        # print(vertice,end=" ")
        visited.add(vertice)
        for neighbor in graph[vertice]:
            dfs_traversal(neighbor,visited)
dfs_traversal(0,set())

def provinces():
    count = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            count += 1
            dfs_traversal(i,visited)
    return count
print(provinces())