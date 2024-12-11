import dis
import queue
from common.graph import Graph

class Solution:
    def dfs(self,vertex,visited,graph):
        if vertex not in graph:
            print(f"{vertex} not in graph")
            return
        if visited[vertex] == 0:
            visited[vertex] = 1
            for neighbor in graph[vertex]:
                self.dfs(neighbor,visited,graph)
            
    def bfs(self,vertex,graph):
        queue = [vertex]
        visited = {node:0 for node in graph}
        while queue:
            current = queue.pop(0)
            visited[current] = 1
            for neighbor in graph[current]:
                if visited[neighbor] == 0 and neighbor not in queue:
                    queue.append(neighbor)
    
    def no_of_provinces(self,graph):
        count = 0
        visited = {node:0 for node in graph}
        for node in graph:
            if visited[node] == 0:
                count += 1
                self.dfs(node,visited,graph)
        print(count)
            
    def rotten_oranges(self,grid):
        freshOranges = 0
        rottenOranges = []
        
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rottenOranges.append((row,col,1))
                elif grid[row][col] == 1:
                    freshOranges += 1
                    
        if freshOranges == 0:
            return 0
        
        while rottenOranges:
            row,col,step = rottenOranges.pop(0)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            newlyRottenOranges = []
            for x,y in directions:
                if 0<=x<rows and 0<=y<cols and grid[x][y] == 1:
                    grid[x][y] = 2
                    freshOranges -= 1
                    newlyRottenOranges.append((x,y,step+1))
                    if freshOranges == 0:
                        print(step)
                        return
            if newlyRottenOranges:
                rottenOranges.extend(newlyRottenOranges)
                    
    def flood_fill(self,start,end,color,image):
        rows = len(image)
        cols = len(image[0])
        
        originalColor = image[start][end]
        if originalColor == color:
            return image
        
        image[start][end] = color
        queue = [(start,end)]
        while queue:
            row,col = queue.pop(0)
            directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            for x,y in directions:
                if 0 <= x < rows and 0 <= y < cols and image[x][y] == 1:
                    image[x][y] = color
                    queue.append((x,y))
        print(image)
        
    def delect_cycle_undireted_bfs(self,vertex,graph):
        visited = {node:0 for node in graph}
        queue = [(vertex,-1)]
        while queue:
            vertex,parent = queue.pop(0)
            if visited[vertex] == 1:
                print("Cycle Found")
                return
            visited[vertex] = 1
            for neighbor in graph[vertex]:
                if neighbor != parent:
                    queue.append((neighbor,vertex))
        print("no cycle found!")
        return
        
    def detect_cycle_undirected_dfs(self,graph):
        def dfs(node,parent,visited):
            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] == 1 and neighbor != parent:
                    return True
                elif visited[neighbor] == 0:
                    if dfs(neighbor, node, visited):
                        return True
            return False
        visited = {node:0 for node in graph}
        for node in graph:
            if visited[node] == 0:
               if dfs(node,-1,visited) == True:
                   print("cycle found!")
                   return
        print('cycle not found!')
        return
    
    def topological_sort_using_dfs(self,graph):
        def dfs(node,visited,result):
            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    dfs(neighbor,visited,result)
            result.append(node)
            
        visited = {node:0 for node in graph}
        result = []
        for node in graph:
            if visited[node] == 0:
                dfs(node,visited,result)
        result = result[::-1]
        print(result)
        
    def topological_sort_using_bfs(self,graph):
        indegree = {node:0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        print(result)
        
    def course_schedule(self,numCourses,prerequisites):
        adjList = {node:[] for node in range(numCourses)}
        for dest,src in prerequisites:
            adjList[src].append(dest)
        
        indegree = {node:0 for node in adjList}
        for node in adjList:
            for neighbor in adjList[node]:
                indegree[neighbor] += 1
        
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor in adjList[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if numCourses == len(result):
            print("No Cycle")
        else:
            print("Cycle Found!")
        
    
    def course_schedule_2(self,numCourses,prerequisites):
        adjList = {node:[] for node in range(numCourses)}
        for dest,src in prerequisites:
            adjList[src].append(dest)
        
        indegree = {node:0 for node in adjList}
        for node in adjList:
            for neighbor in adjList[node]:
                indegree[neighbor] += 1
        
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor in adjList[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(result) == numCourses:
            print(result)
        else:
            print([])
            
    def create_adj_from_graph(self,graph):
        adjList = {node:[] for node in range(len(graph))}
        for index,values in enumerate(graph):
            for value in values:
                adjList[index].append(value)
        print(adjList)
    
    def find_even_state_safe(self,graph):
        adjList = {node:[] for node in range(len(graph))}
        for src,neighbors in enumerate(graph):
            for dest in neighbors:
                adjList[dest].append(src)
                
        outdegree = {node:0 for node in adjList}
        for node in adjList:
            for neighbor in adjList[node]:
                outdegree[neighbor] += 1
        
        queue = []
        for node in outdegree:
            if outdegree[node] == 0:
                queue.append(node)
        
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor in adjList[current]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)
        result = sorted(result)
        print(result)
        
    
    def find_shortest_distance_directed_acyclic_graph(self,graph,source):
        indegree = {node:0 for node in graph}
        for node in graph:
            for neighbor,weight in graph[node]:
                indegree[neighbor] += 1
        
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        stack = []
        while queue:
            current = queue.pop(0)
            stack.append(current)
            for neighbor,weight in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        distance = {node:float("inf") for node in graph}
        distance[source] = 0
        while stack:
            current = stack.pop(0)
            if distance[current] != float("inf"):
                for neighbor,weight in graph[current]:
                    if distance[neighbor] > distance[current] + weight:
                        distance[neighbor] = distance[current]+weight
        print(distance)
        
    
    def find_shortest_distance_undirected_acyclic_graph(self,graph,source,totalNodes,totalEdges):
        adjList = {node:[] for node in range(totalNodes)}
        for u,v in graph:
            adjList[u].append(v)
            adjList[v].append(u)
        
        distance = {node:float("inf") for node in range(totalNodes)}
        distance[source] = 0
        
        queue = [(source,0)] #(node,dist)
        while queue:
            node,dist = queue.pop(0)
            for neighbor in adjList[node]:
                if distance[neighbor] == float("inf"):
                    distance[neighbor] = distance[node] + 1
                    queue.append((neighbor,distance[node]+1))
        print(distance)
        
        
        
        
        
        
        
            


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
sol.no_of_provinces(g.graph)

grid = [[2,1,1],[1,1,0],[0,1,1]]
sol.rotten_oranges(grid)

image = [[1,1,1],[1,1,0],[1,0,1]]
sol.flood_fill(1,1,2,image)

sol.delect_cycle_undireted_bfs(1,g.graph)
sol.detect_cycle_undirected_dfs(g.graph)


matrix = {
    5 : [0,2],
    2 : [3],
    0 : [],
    1 : [],
    3 : [1],
    4 : [0,1],
}
# sol.topological_sort_using_dfs(matrix)
# sol.topological_sort_using_bfs(matrix)
# sol.course_schedule(2,[[0,1],[1,0]])
# sol.course_schedule_2(4,[[1,0],[2,0],[3,1],[3,2]])
# sol.create_adj_from_graph([[1,2],[2,3],[5],[0],[5],[],[]])
# sol.find_even_state_safe([[1,2],[2,3],[5],[0],[5],[],[]])

graph = {
    6 : [(4,2),(5,3)],
    5 : [{4,1}],
    4 : [(0,3),(2,1)],
    3 : [],
    2 : [(3,3)],
    1 : [(3,1)],
    0 : [(1,2)]
}
sol.find_shortest_distance_directed_acyclic_graph(graph,6)
sol.find_shortest_distance_undirected_acyclic_graph([[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]],0,9,10)