from common.graph import Graph


class Solution:
    def dfs_traversal(self,node,visited,graph):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                self.dfs_traversal(neighbor,visited,graph)
    
    def noOfProvinces(self,graph):
        count = 0
        visited = set()
        for node in graph:
            if node not in visited:
                count += 1
                self.dfs_traversal(node,visited,graph)
        print("Total Number Of Provinces ---> ",count)
            


g = Graph()
# provinces - 1
g.addVertice(1)
g.addVertice(2)
g.addVertice(3)
g.addEdge(1,2)
g.addEdge(2,3)
# provinces - 2
g.addVertice(4)
g.addVertice(5)
g.addVertice(6)
g.addEdge(4,5)
g.addEdge(5,6)
# provinces - 3
g.addVertice(7)
g.addVertice(8)
g.addEdge(7,8)
# provinces - 4
g.addVertice(10)
g.addVertice(11)
g.addVertice(12)
g.addVertice(13)
g.addVertice(14)
g.addEdge(10,11)
g.addEdge(11,12)
g.addEdge(12,13)
g.addEdge(13,14)


sol = Solution()
sol.noOfProvinces(g.graph)