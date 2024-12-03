class Graph:
    def __init__(self):
        self.graph = {}
    
    def addVertice(self,newVertice):
        if newVertice in self.graph:
            print(f"{newVertice} vertice already present!")
            return
        else:
            self.graph[newVertice] = []
            # print(f"{newVertice} vertice added successfully!")
            return
    
    def addEdge(self,vertice1,vertice2):
        if vertice1 not in self.graph:
            print(f"{vertice1} vertice not present in vertices")
            return
        elif vertice2 not in self.graph:
            print(f"{vertice2} vertice not present in vertices")
            return
        else:
            self.graph[vertice1].append(vertice2)
            self.graph[vertice2].append(vertice1)
            # print(f"edge added between vertices {vertice1} and {vertice2}")
            return
        
    def removeVertice(self,targetVertice):
        if targetVertice not in self.graph:
            print(f"{targetVertice} vertice not present in vertices")
            return
        else:
            self.graph.pop(targetVertice)
            for key in self.graph:
                lists = self.graph[key]
                if targetVertice in lists:
                    lists.remove(targetVertice)
    
    def removeEdge(self,vertice1,vertice2):
        if vertice1 not in self.graph:
            print(f"{vertice1} vertice not present in vertices!")
            return
        elif vertice2 not in self.graph:
            print(f"{vertice2} vertice not present in vertices!")
            return
        else:
            self.graph[vertice1].remove(vertice2)
            self.graph[vertice2].remove(vertice1)
            # print(f"edge between vertices {vertice1} and {vertice2} has been removed!")
            return
    
    def DFS(self,initialVertice,visited):
        if initialVertice not in self.graph:
            print(f"{initialVertice} vertice not in graph!")
            return
        if initialVertice not in visited:
            visited.add(initialVertice)
            print(initialVertice,end=" ")
            for neighbor in self.graph[initialVertice]:
                self.DFS(neighbor,visited)
                
            
        
    
    
g = Graph()
g.addVertice("A")
g.addVertice("B")
g.addVertice("C")
g.addVertice("D")
g.addVertice("E")
g.addVertice("F")

g.addEdge("A","B")
g.addEdge("A","C")
g.addEdge("A","D")
g.addEdge("B","D")
g.addEdge("C","D")
g.addEdge("B","E")
g.addEdge("D","E")
g.addEdge("E","F")

g.DFS("A",set())