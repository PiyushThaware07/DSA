
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


g = Graph()
g.add_vertices("A")
g.add_vertices("B")
g.add_vertices("C")
g.add_vertices("D")
print(g.graph)
g.add_edge("A","B")
g.add_edge("D","B")
print(g.graph)
