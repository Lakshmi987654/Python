def create_checkerboard(rows, cols, char1='X', char2='O'):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            # Choose char1 or char2 based on position to create checkerboard effect
            if (r + c) % 2 == 0:
                row.append(char1)
            else:
                row.append(char2)
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Example usage
rows, cols = 8, 8
checkerboard = create_checkerboard(rows, cols)
print_grid(checkerboard)
