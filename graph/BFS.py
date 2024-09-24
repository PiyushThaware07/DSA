def BFS_Traversal(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = [start]  # Initialize the queue with the start node

    while queue:
        vertice = queue.pop(0)  # Dequeue a vertex from the front of the queue
        if vertice not in visited:
            print(vertice, end=" ")  # Process the vertex (print it)
            visited.add(vertice)  # Mark the vertex as visited
            
            # Enqueue all unvisited neighbors
            for neighbor in graph[vertice]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue

# Example graph as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# Perform BFS starting from node 0
print("BFS Traversal starting from node 0:")
BFS_Traversal(graph, 0)
