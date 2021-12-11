import dataclasses
import sys
from itertools import repeat

import common


@dataclasses.dataclass
class Grid:
    rows = []

    def get(self, row, col):
        return self.rows[row][col]

    def addrow(self, row):
        self.rows.append(row)

    def rowcount(self):
        return len(self.rows)

    def colcount(self):
        return len(self.rows[0])


def sum_of_low_points(grid):
    sum_of_points = 0
    for row in range(0, grid.rowcount()):
        for col in range(0, grid.colcount()):
            cell = grid.get(row, col)
            # get the adjacent cell values
            north = grid.get(row-1, col) if row > 0 else sys.maxsize
            south = grid.get(row+1, col) if row < grid.rowcount()-1 else sys.maxsize
            east = grid.get(row, col+1) if col < grid.colcount()-1 else sys.maxsize
            west = grid.get(row, col-1) if col > 0 else sys.maxsize
            # check if the current cell is lower than all of them
            if all(value > cell for value in [north, south, east, west]):
                sum_of_points += (cell + 1)
    return sum_of_points


def traverse(grid, traversed, row, col):
    # standard A* - recursively consume the grid until we hit 9's or already traversed cells,
    # totalling as we go, and returning the number of cells we traversed. 
    if row < 0 or row >= grid.rowcount() or col < 0 or col >= grid.colcount():
        return 0
    if traversed[row][col]:
        return 0
    traversed[row][col] = True
    if grid.get(row, col) == 9:
        return 0
    num_cells_traversed = 1
    num_cells_traversed += traverse(grid, traversed, row-1, col)
    num_cells_traversed += traverse(grid, traversed, row+1, col)
    num_cells_traversed += traverse(grid, traversed, row, col-1)
    num_cells_traversed += traverse(grid, traversed, row, col+1)
    return num_cells_traversed


def find_basins(grid):
    basins = []
    traversed = [list(repeat(False, grid.colcount())) for _ in range(0, grid.rowcount())]
    for row in range(0, grid.rowcount()):
        for col in range(0, grid.colcount()):
            total = traverse(grid, traversed, row, col)
            if total > 0:
                basins.append(total)
    return basins


data = common.read_all_data("input/day9.txt")
datagrid = Grid()
for line in data:
    row = [int(digit) for digit in line]
    datagrid.addrow(row)
total = sum_of_low_points(datagrid)
print(f"(Part 1) Sum of all low points: {total}")

all_basins = sorted(find_basins(datagrid), reverse=True)
result = all_basins[0] * all_basins[1] * all_basins[2]
print(f"(Part 2) Three largest basin sizes multipled: {result}")
