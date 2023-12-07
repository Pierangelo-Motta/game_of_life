import pygame
import random

# Initialize Pygame
pygame.init()

# Define the size of the grid and the size of each cell
SIZE = 200
CELL_SIZE = 5

# Create a window to display the grid
screen = pygame.display.set_mode((SIZE * CELL_SIZE, SIZE * CELL_SIZE))

# Initialize the game clock
clock = pygame.time.Clock()

# Create the initial grid
grid = [[random.randint(0, 1) for _ in range(SIZE)] for _ in range(SIZE)]

# Main loop
running = True
while running:
    clock.tick(60)
    # Draw the grid
    for x in range(SIZE):
        for y in range(SIZE):
            if grid[x][y] == 1:
                color = (0, 255, 0)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the grid based on the game's rules
    new_grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for x in range(SIZE):
        for y in range(SIZE):
            # Count the number of alive neighbors
            alive_neighbors = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < SIZE and 0 <= ny < SIZE:
                        alive_neighbors += grid[nx][ny]

            # Update the cell's state
            if grid[x][y] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[x][y] = 0
                else:
                    new_grid[x][y] = 1
            else:
                if alive_neighbors == 3:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0

    # Replace the old grid with the new one
    grid = new_grid

# Quit Pygame
pygame.quit()