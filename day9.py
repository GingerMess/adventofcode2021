import dataclasses
import sys

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


data = common.read_all_data("input/day9.txt")
grid = Grid()
for line in data:
    row = [int(digit) for digit in line]
    grid.addrow(row)
sum_of_low_points = 0
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
            sum_of_low_points += (cell + 1)

print(f"(Part 1) Sum of all low points: {sum_of_low_points}")
