from typing import List, Literal

Alive = Literal[1]
Dead = Literal[0]
Row = List[Dead | Alive]
Grid = List[Row]

ALIVE: Alive = 1
DEAD: Dead = 0


def _get_neighbours(grid: Grid, row: int, col: int) -> int:
    no_rows = len(grid)
    no_cols = len(grid[0])
    neighbours = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            # TODO non square grid
            if r >= 0 and r < no_rows and c >= 0 and c < no_cols and not (r == row and c == col):
                neighbours += grid[r][c]
    return neighbours


def next_generation(grid: Grid) -> Grid:
    no_rows = len(grid)
    no_cols = len(grid[0])
    new_grid: Grid = [[DEAD for _ in range(
        no_cols)] for _ in range(no_rows)]
    for i in range(no_rows):
        for j in range(no_cols):
            neighbours = _get_neighbours(grid, i, j)
            if grid[i][j] == ALIVE:
                new_grid[i][j] = ALIVE if neighbours in (2, 3) else DEAD
            else:
                new_grid[i][j] = ALIVE if neighbours == 3 else DEAD
    return new_grid
