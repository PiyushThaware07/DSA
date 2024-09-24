
# * Insertion using Adjacency List 
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
                


g = Graph()
g.add_vertices("A")
g.add_vertices("B")
g.add_vertices("C")
g.add_vertices("D")
g.add_vertices("E")
g.add_vertices("F")
g.add_vertices("G")
g.add_vertices("H")
print(g.graph)
g.add_edge("A","B")
g.add_edge("D","B")
g.add_edge("D","H")
g.add_edge("D","F")
g.add_edge("F","A")
g.add_edge("F","E")
print(g.graph)
g.DFS("A",set())