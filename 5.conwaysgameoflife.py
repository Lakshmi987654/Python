import time
import os
import random

def clear_screen():
    # Clear the console screen (works on Windows and Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid(rows, cols):
    # Create a grid with random 0s and 1s
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        print(''.join('█' if cell else ' ' for cell in row))

def get_neighbors(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    neighbors = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i == row and j == col) or i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            neighbors += grid[i][j]
    return neighbors

def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(grid, i, j)
            if grid[i][j] == 1:
                # Any live cell with two or three live neighbors survives.
                if neighbors == 2 or neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                # Any dead cell with exactly three live neighbors becomes a live cell.
                if neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
    return new_grid

def game_of_life(rows=20, cols=50, generations=100, delay=0.2):
    grid = create_grid(rows, cols)
    for _ in range(generations):
        clear_screen()
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(delay)

# Run the game
game_of_life()
