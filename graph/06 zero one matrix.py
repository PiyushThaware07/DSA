mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]

rows = len(mat)
cols = len(mat[0])

# Initialize 'visited' and 'distance' as 2D matrices
visited = [[0 for _ in range(cols)] for _ in range(rows)]
distance = [[0 for _ in range(cols)] for _ in range(rows)]
queue = []

# Iterate through the matrix to find cells with value 1
for row in range(rows):
    for col in range(cols):
        if mat[row][col] == 0:
            visited[row][col] = 1
            queue.append((row, col, 0))
            distance[row][col] = 0

while queue:
    row,col,step = queue.pop(0)
    directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
    for x,y in directions:
        if x >= 0 and x < rows and y >= 0 and y < cols and visited[x][y] == 0:
            visited[x][y] = 1
            queue.append((x,y,step+1))
            distance[x][y] = step + 1
print(distance)

