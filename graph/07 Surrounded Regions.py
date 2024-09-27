mat = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
    ]
rows = len(mat)
cols = len(mat[0])

def dfs_traversal(row,col,visited):
    visited[row][col] = 1
    directions = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
    for x,y in directions:
        if x>=0 and x<rows and y>=0 and y<cols and visited[x][y] == 0 and mat[x][y] == "O":
            dfs_traversal(x,y,visited)



visited = [[0 for _ in range(cols)] for _ in range(rows)]

# top row
for col in range(cols):
    if visited[0][col] == 0 and mat[0][col] == "O":
        dfs_traversal(0,col,visited)

# bottom row
for col in range(cols):
    if visited[rows-1][col] == 0 and mat[rows-1][col] == "O":
        dfs_traversal(rows-1,col,visited)

# left col
for row in range(rows):
    if visited[row][0] == 0 and mat[row][0] == "O":
        dfs_traversal(row,0,visited)

# right col
for row in range(rows):
    if visited[row][cols-1] == 0 and mat[row][cols-1] == "O":
        dfs_traversal(row,cols-1,visited)

for row in range(rows):
    for col in range(cols):
        if mat[row][col] == "O" and visited[row][col] == 0:
            mat[row][col] = "X"

for row in mat:
    print(row)