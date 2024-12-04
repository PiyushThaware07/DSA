# PROBLEM STATEMENT : It determines if there is a cycle in an undirected graph starting from a given node.

class Solution:
    def BFS_Traversal(self,graph,start):
        visited = set()                      # To keep track of visited nodes
        queue = [(start,-1)]                 # Initialize queue with the starting node and its parent (-1 indicates no parent)
        
        # Perform BFS
        while queue:
            vertice,parent = queue.pop()     # Dequeue the next node and its parent
            if vertice in visited:           # If the current node is already visited, a cycle is detected
                return True
            visited.add(vertice)             # Mark the node as visited
            
            # Add unvisited neighbors to the queue
            for neighbor in graph[vertice]:
                # Ignore the node that is the parent (avoid backtracking to the parent)
                if neighbor != parent:
                    queue.append((neighbor,vertice)) # Enqueue the neighbor with its parent
        return False # Return False if no cycle is found



graph = {
    0: [1, 2],    
    1: [0, 3, 4], 
    2: [0, 5],    
    3: [1, 5],    
    4: [1],       
    5: [2, 3]    
}
sol = Solution()
print(sol.BFS_Traversal(graph,0))