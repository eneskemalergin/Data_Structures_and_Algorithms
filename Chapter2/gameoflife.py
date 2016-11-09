# Main program that plays the game of life.
from life import LifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [(1,1), (1,2), (2,2), (3,2)]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 8

def main():
    # Construct the game grid and configure it.
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Play the game
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)

# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    liveCells = list()

    # Iterate over the elements of the grid.
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            # Determine the number of live neighbors for this cells
            neighbors = grid.numLiveNeighbors(i,j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation
            if (neighbors == 2  and grid.isLiveCell(i,j)) or (neighbors ==3):
                liveCells.append((i,j))

    # Reconfigure the grid using liveCells coord list.
    grid.configure(liveCells)

# Prints a text-based representation of the game grid.
def draw(grid):
    pass

# Executes the main routine.
if __name__ == '__main__':
    main()
