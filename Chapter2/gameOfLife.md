## The Game of Life

The game of life devised by British mathematician John H. Conway, is a Soltaire-type game that is analogous with "the rise, fall and alternations of society of living organism."

*Zero-player game :)* was introduced by Martin Gardner. After that the game of life became very popular and much observed to understand how complex systems or patterns can evolve from a simple set of rules.

**Was an early example of a problem in the modern field of mathematics called cellular automata.**

### Rules of the Game

The game uses an infinite-sized rectangular grid of cells in which each cell is either empty or occupied by an organism. The occupied cells are said to be alive, whereas the empty ones are dead. The game is played over a specific period of time with each turn creating a new *"generation"* based on the arrangement of live organisms in the current configuration. The status of a cell in the next generation is determined by applying the following four basic rules to each cell in the current configuration:

1. If a cell is alive and has either two or three live neighbors, the cell remains alive in the next generation. The neighbors are the eight cells immediately surrounding a cell: vertically, horizontally, and diagonally.
2. A living cell that has no live neighbors or a single live neighbor dies from isolation in the next generation
3. A living cell that has four or more live neighbors dies from overpopulation in the next generation.
4. A dead cell with exactly three live neighbors results in a birth and becomes alive in the next generation. All other dead cells remain dead in the next generation.



So the game starts with an initial configuration supplied by the user.
