def rottingOrange(grid):
    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Count fresh oranges and track rotten ones
    fresh_oranges = 0
    rotten_oranges = []

    # Loop through the grid to initialize the counts
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Fresh orange found
                fresh_oranges += 1
            elif grid[row][col] == 2:  # Rotten orange found
                rotten_oranges.append((row, col))

    # If there are no fresh oranges, no time is needed
    if fresh_oranges == 0:
        return 0

    # Initialize the minutes counter
    minutes = 0

    # Continue until no more rotten oranges are spreading
    while len(rotten_oranges) != 0:
        minutes += 1
        new_rotten_oranges = []  # Track newly rotten oranges in this round

        # Process all current rotten oranges
        for row, col in rotten_oranges:
            # Check adjacent cells (up, down, left, right)
            directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            for i, j in directions:
                # Ensure the cell is within bounds and contains a fresh orange
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                    grid[i][j] = 2  # Rot the fresh orange
                    fresh_oranges -= 1  # Decrease the count of fresh oranges
                    new_rotten_oranges.append((i, j))  # Add to the new list of rotten oranges
                    # If all fresh oranges have rotted, return the elapsed minutes
                    if fresh_oranges == 0:
                        return minutes

        # Update the rotten oranges list with newly rotten ones
        rotten_oranges = new_rotten_oranges

    # If there are still fresh oranges after all possible spreading, return -1
    return -1 if fresh_oranges > 0 else minutes


# Example usage
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(rottingOrange(grid))  # Output should be 4
