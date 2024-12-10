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
                   
    def topological_sort_dfs(self,matrix):
        def dfs(node,visited,result):
            visited[node] = 1
            for neighbor in matrix[node]:
                if visited[neighbor] == 0:
                    dfs(neighbor,visited,result)
            result.append(node)
            
        visited = {node:0 for node in matrix}
        result = []
        for node in matrix:
            if visited[node] == 0:
                dfs(node,visited,result)
        print(result[::-1])
            
    def topological_sort_bfs(self,matrix):
        indegree = {node:0 for node in matrix}
        for node in matrix:
            for neighbor in matrix[node]:
                indegree[neighbor] += 1
        queue = []
        for node in matrix:
            if indegree[node] == 0:
                queue.append(node)
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor in matrix[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        print(result)
            
        
        
        
        
        
        
        
        
            


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
sol.topological_sort_dfs(matrix)
sol.topological_sort_bfs(matrix)