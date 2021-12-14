import dataclasses
from itertools import repeat

import common


class Grid:
    octopuses = []

    def addrow(self, row):
        self.octopuses.append(row)

    def rows(self):
        return len(self.octopuses)

    def cols(self):
        return len(self.octopuses[0])

    def get(self, row, col):
        return self.octopuses[row][col]

    def increment(self, row, col):
        if row < 0 or row >= self.rows() or col < 0 or col >= self.cols():
            return
        self.octopuses[row][col] += 1

    def check(self, row, col, flashed):
        if row < 0 or row >= self.rows() or col < 0 or col >= self.cols():
            return
        if not flashed[row][col] and self.octopuses[row][col] > 9:
            self.flash(row, col, flashed)

    def step(self):
        # increment all energy levels by 1
        for row in range(0, self.rows()):
            for col in range(0, self.cols()):
                self.increment(row, col)
        # track which octopuses have flashed
        flashed = [list(repeat(False, self.cols())) for _ in range(0, self.rows())]
        # check each octopus, recursively if they flash
        for row in range(0, self.rows()):
            for col in range(0, self.cols()):
                self.check(row, col, flashed)
        # count and return how many flashes this step, and reset flashed octopuses to 0 energy
        flash_total = 0
        for row in range(0, self.rows()):
            for col in range(0, self.cols()):
                if flashed[row][col]:
                    # set the energy level to 0
                    self.octopuses[row][col] = 0
                    flash_total += 1
        return flash_total

    def flash(self, row, col, flashed):
        if flashed[row][col]:
            return
        flashed[row][col] = True
        self.increment(row-1, col-1)
        self.increment(row-1, col)
        self.increment(row-1, col+1)
        self.increment(row, col-1)
        self.increment(row, col+1)
        self.increment(row+1, col-1)
        self.increment(row+1, col)
        self.increment(row+1, col+1)
        self.check(row-1, col-1, flashed)
        self.check(row-1, col, flashed)
        self.check(row-1, col+1, flashed)
        self.check(row, col-1, flashed)
        self.check(row, col+1, flashed)
        self.check(row+1, col-1, flashed)
        self.check(row+1, col, flashed)
        self.check(row+1, col+1, flashed)

    def __str__(self):
        str = ""
        for row in self.octopuses:
            str += f"{row}\n"
        return str

    def __repr__(self) -> str:
        return self.__str__()


grid = Grid()
data = common.read_all_data("input/day11.txt")
for line in data:
    grid.addrow([int(char) for char in line])
total = 0
print(f"Start:\n{grid}")
for i in range(0, 10000):
    flashes_this_step = grid.step()
    # print(f"Step {i+1}:\n{grid}")
    if i < 100:
        total += flashes_this_step
    if flashes_this_step == grid.rows() * grid.cols():
        print(f"(Part 2) All flashed in step {i+1}")
        print(f"{grid}")
        break
print(f"(Part 1) Total Flashes for 100 steps: {total}")
