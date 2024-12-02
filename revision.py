class Graph:
    def __init__(self):
        self.vertices = {}
        
    
    def addVertices(self,newVertice):
        if newVertice in self.vertices:
            print(f"{newVertice} node already exists in graph!")
            return
        else:
            self.vertices[newVertice] = []
            print(f"{newVertice} hash been added successfully!")
            return
    
    def addEdges(self,vertice1,vertice2):
        if vertice1 not in self.vertices:
            print(f"{vertice1} node not found!")
            return
        elif vertice2 not in self.vertices:
            print(f"{vertice2} node not found!")
            return
        else:
            self.vertices[vertice1].append(vertice2)
            self.vertices[vertice2].append(vertice1)
            print(f"link between {vertice1} and {vertice2} has been added!")
            return
    
    def depthFirstSearch(self,root,visited=set()):
        if root not in self.vertices:
            print(f"{root} not in vertices!")
            return
        if root not in visited:
            visited.add(root)
            print(root,end="-> ")
            for neighbor in self.vertices[root]:
                self.depthFirstSearch(neighbor,visited)
            print()
            
    
    
root = Graph()
root.addVertices("A")
root.addVertices("B")
root.addVertices("C")
root.addVertices("D")
root.addEdges("A","B")
root.addEdges("A","D")
root.addEdges("B","C")
root.depthFirstSearch("A")
print(root.vertices)