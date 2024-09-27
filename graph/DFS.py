
# * Insertion using Adjacency List 
from calendar import c
from operator import neg


class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertices(self,value):
        if value in self.graph:
            print(f"{value} node is already present in node list")
            return
        else:
            self.graph[value] = []
            print(f"Node {value} added.")
    
    def add_edge(self,vertice1,vertice2):
        if vertice1 not in self.graph:
            print(f"{vertice1} node is not present in node list")
            return
        elif vertice2 not in self.graph:
            print(f"{vertice2} node is not present in node list")
            return
        else:
            self.graph[vertice1].append(vertice2)
            self.graph[vertice2].append(vertice1)  # comment this line in case of directed graph or directed weighted graph
            print(f"Edge between {vertice1} and {vertice2} added.")
            return
    
    def DFS(self, vertice, visited):
        """Performs Depth-First Search (DFS) traversal starting from a vertex."""
        if vertice not in self.graph:
            print(f"{vertice} node is not present in node list")
            return
        if vertice not in visited:
            print(vertice, end=" ")
            visited.add(vertice)
            for neighbor in self.graph[vertice]:
                self.DFS(neighbor, visited)
            print()
    
    def checkCycle(self, start, visited, parent):
        # Mark the current node as visited
        visited[start] = 1

        # Traverse all the neighbors of the current node
        for neighbor in self.graph[start]:
            # If the neighbor has already been visited
            if visited[neighbor] != 0:
                # Check if the visited neighbor is not the parent node
                # If the neighbor is not the parent, a cycle is found
                if neighbor != parent:
                    return True
            # If the neighbor has not been visited yet
            else:
                # Recursively check for a cycle starting from the neighbor
                if self.checkCycle(neighbor, visited, start):
                    return True
        
        # No cycle detected from this path
        return False


    def isCycle(self):
        # Initialize a visited list, setting all nodes to unvisited (0)
        visited = [0] * len(self.graph)

        # Iterate through all nodes in the graph
        for i in self.graph:
            # If the node has not been visited
            if visited[i] == 0:
                # Call checkCycle to detect if there's a cycle starting from node i
                # -1 is passed as the initial parent since the first node has no parent
                if self.checkCycle(i, visited, -1):
                    print("Cycle detected")
                    return True
        
        # If no cycle is found in the graph
        print("Cycle not detected")
        return False



g = Graph()
g.add_vertices(1)
g.add_vertices(2)
g.add_vertices(3)
g.add_vertices(4)
g.add_vertices(5)
g.add_vertices(6)
g.add_vertices(7)
g.add_vertices(8)
print(g.graph)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,3)
g.add_edge(6,7)
g.add_edge(7,2)
g.add_edge(8,7)
print(g.graph)
g.DFS(1,set())
g.isCycle()