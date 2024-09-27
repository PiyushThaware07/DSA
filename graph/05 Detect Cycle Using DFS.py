class Graph:
    def __init__(self):
        self.graph = {}

    def insert_vertice(self,vertice):
        if vertice in self.graph:
            print(f"{vertice} node is already present in node list")
            return
        else:
            self.graph[vertice] = []
            print(f"Node {vertice} added.")
    
    def insert_edge(self,vertice1,vertice2):
        if vertice1 not in self.graph:
            print(f"{vertice1} is not present")
            return
        elif vertice2 not in self.graph:
            print(f"{vertice2} is not present")
            return
        else:
            self.graph[vertice1].append(vertice2)
            self.graph[vertice2].append(vertice1)
            print(f"Edge between {vertice1} and {vertice2} added.")
            return
    
    def dfs_traversal(self,start,visited = set()):
        if start not in self.graph:
            print(f"{start} vertice not present")
            return
        
        if start not in visited:
            print(start,end = " ")
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs_traversal(neighbor,visited)

    
g = Graph()
g.insert_vertice("A")
g.insert_vertice("B")
g.insert_vertice("C")
g.insert_vertice("D")
g.insert_vertice("E")
g.insert_vertice("F")
print(g.graph)
g.insert_edge("A","B")
g.insert_edge("B","C")
g.insert_edge("C","E")
g.insert_edge("D","F")
g.insert_edge("A","F")
print(g.graph)
g.dfs_traversal("A")