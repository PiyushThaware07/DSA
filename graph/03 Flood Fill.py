# Input image represented as a 2D list (matrix) where each element is either 1 or 0
image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]

# Starting row and column for the flood fill algorithm
sr = 1  # Starting row index
sc = 1  # Starting column index
color = 2  # New color to fill the area with

def solution():
    # Determine the number of rows and columns in the image matrix
    rows = len(image)
    cols = len(image[0])

    # Get the original color of the starting pixel
    original_color = image[sr][sc]
        
    # If the original color is the same as the new color, no need to proceed
    if original_color == color:
            return image
    
    # Set the starting point in the image to the new color
    image[sr][sc] = color
    
    # Initialize a queue to keep track of the pixels to process (starting with the given starting point)
    temp = [(sr, sc)]
    
    # Continue processing until no more pixels are left in the queue
    while len(temp) != 0:
        # Get the current pixel (row, col) from the queue
        row, col = temp.pop(0)
        
        # Define the four possible directions (up, down, left, right) to check adjacent pixels
        directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        
        # Loop through each direction
        for x, y in directions:
            # Check if the adjacent pixel is within the bounds of the image and is still the original color (1)
            if x >= 0 and x < rows and y >= 0 and y < cols and image[x][y] == original_color:
                # Change the adjacent pixel to the new color
                image[x][y] = color
                # Add the pixel to the queue for further processing
                temp.append((x, y))
    
    # Print the modified image after the flood fill operation
    print(image)

# Run the solution function to apply flood fill and print the result
solution()
