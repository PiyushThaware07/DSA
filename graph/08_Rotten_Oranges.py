class Solution:
    def __init__(self, graph):
        self.graph = graph

    def rottenOranges(self):
        # 1. Get dimensions
        rows = len(self.graph)
        cols = len(self.graph[0])
        
        # 2. Initialize to get coordinates of rotten oranges and fresh orange count
        totalFreshOranges = 0
        rottenOranges = []
        for row in range(rows):
            for col in range(cols):
                if self.graph[row][col] == 1:
                    totalFreshOranges += 1
                elif self.graph[row][col] == 2:
                    rottenOranges.append((row, col))
        
        # 3. If no fresh oranges, return 0 minutes
        if totalFreshOranges == 0:
            return 0
        
        # 4. Start rotting oranges using BFS
        minutes = 0
        while rottenOranges:
            newlyRottenOranges = []
            for row, col in rottenOranges:
                # Check all 4 possible directions
                directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for i, j in directions:
                    if 0 <= i < rows and 0 <= j < cols and self.graph[i][j] == 1:
                        self.graph[i][j] = 2  # Mark as rotten
                        totalFreshOranges -= 1  # Reduce fresh orange count
                        newlyRottenOranges.append((i, j))
            
            # If new oranges became rotten, increment time
            if newlyRottenOranges:
                minutes += 1
            rottenOranges = newlyRottenOranges
        
        # 5. Check if any fresh oranges remain
        if totalFreshOranges > 0:
            return -1  # Not all oranges can be rotted
        return minutes


# Test the implementation
grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution(grid)
print(sol.rottenOranges())  # Output should be 2
