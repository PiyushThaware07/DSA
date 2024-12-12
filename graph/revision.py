class Solution:
    def dijkstra(self,graph,source,destination):
        distances = {node:float("inf") for node in graph}
        distances[source] = 0
        
        parent = {node:None for node in graph}
        
        queue = [(source,0)]
        visited = set()
        while queue:
            minNode = queue[0][0]
            minDist = queue[0][1]
            minIndex = 0
            for index in range(1,len(queue)):
                currentNode = queue[index][0]
                currentDist = queue[index][1]
                if currentDist < minDist:
                    minDist = currentDist
                    minNode = currentNode
                    minIndex = index
            queue.pop(minIndex)
            
            if minNode == destination:
                break
            
            if minNode in visited:
                continue
            visited.add(minNode)
            
            for neighbor,weight in graph[minNode]:
                newDist = minDist + weight
                if distances[neighbor] > newDist:
                    distances[neighbor] = newDist
                    parent[neighbor] = minNode
                    queue.append((neighbor,newDist))
        
        path = []
        node = destination
        while node is not None:
            path.append(node)
            node = parent[node]
        path = path[::-1]
        print(path)
        
                    
                
        
                
    

graph = {0: [(1, 4), (2, 1)], 1: [(0, 4), (2, 2), (3, 5)], 2: [(0, 1), (1, 2), (3, 8)], 3: [(1, 5), (2, 8)]}
sol = Solution()
sol.dijkstra(graph,0,3)