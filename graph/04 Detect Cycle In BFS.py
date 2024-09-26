from operator import ne


def BFS_Traversal(graph, start):
    visited = set()  # To track visited nodes
    queue = [(start, -1)]  # (current node, parent node)

    while queue:
        vertice, parent = queue.pop(0)  # Get the current node and its parent

        if vertice in visited:
            # If the node has been visited and it's not the parent, we found a cycle
            print(f"Cycle detected at node {vertice}")
            return True  # Cycle found

        visited.add(vertice)  # Mark the current node as visited

        # Visit all the neighbors
        for neighbor in graph[vertice]:
            if neighbor != parent:  # Don't revisit the parent node
                queue.append((neighbor, vertice))

    return False  # No cycle found

# Example graph
graph = {
    0: [1, 2],    # Node 0 connects to 1 and 2
    1: [0, 3, 4], # Node 1 connects to 0, 3, and 4
    2: [0, 5],    # Node 2 connects to 0 and 5
    3: [1, 5],    # Node 3 connects to 1 and 5 (added this to create a cycle)
    4: [1],       # Node 4 connects to 1
    5: [2, 3]     # Node 5 connects to 2 and 3 (completes the cycle with 3)
}

# Call BFS traversal to detect cycle
if BFS_Traversal(graph, 0):
    print("Graph contains a cycle.")
else:
    print("No cycle detected.")







# ----------------------------------
def isCycle(v, graph):
    visited = [0] * v

    def bfs(start):
        queue = [(start, -1)]
        while queue:
            vertice, parent = queue.pop(0)
            if visited[vertice] == 1:
                return True

            visited[vertice] = 1
            for neighbor in graph[vertice]:
                if neighbor != parent:
                    queue.append((neighbor, vertice))
        return False

    for i in range(v):
        if not visited[i]:
            if bfs(i):
                return True
    return False


graph = {
    0: [1, 2],    # Node 0 connects to 1 and 2
    1: [0, 3, 4], # Node 1 connects to 0, 3, and 4
    2: [0],       # Node 2 connects to 0
    3: [1, 5],    # Node 3 connects to 1 and 5
    4: [1],       # Node 4 connects to 1
    5: [3]        # Node 5 connects to 3
}

print(isCycle(6, graph))  # Output: True (because of the cycle between 1, 3, and 5)
