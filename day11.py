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

    def process(self, row, col, flashed):
        if self.octopuses[row][col] > 9 and not flashed[row][col]:
            self.flash(row, col, flashed)

    def flash(self, row, col, flashed):
        # don't flash anything out of bounds
        if row < 0 or row >= self.rows() or col < 0 or col >= self.cols():
            return
        self.octopuses[row][col] += 1
        if self.octopuses[row][col] > 9 and not flashed[row][col]:
            # we have enough energy to flash
            flashed[row][col] = True
            self.flash(row - 1, col - 1, flashed)
            self.flash(row - 1, col, flashed)
            self.flash(row - 1, col + 1, flashed)
            self.flash(row, col - 1, flashed)
            self.flash(row, col + 1, flashed)
            self.flash(row + 1, col - 1, flashed)
            self.flash(row + 1, col, flashed)
            self.flash(row + 1, col + 1, flashed)

    def step(self):
        # increase all octo-energy by 1
        for row in range(0, self.rows()):
            for col in range(0, self.cols()):
                self.octopuses[row][col] += 1
        # initiate flashing!
        flashed = [list(repeat(False, self.cols())) for _ in range(0, self.rows())]
        for row in range(0, self.rows()):
            for col in range(0, self.cols()):
                self.process(row, col, flashed)
        # set all octo-energy levels to 0 for all octopuses that flashed
        total_flashes = 0
        for row in range(0, self.rows()):
            for col in range(0, self.cols()):
                if flashed[row][col]:
                    self.octopuses[row][col] = 0
                    total_flashes += 1
        return total_flashes

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
for i in range(0, 100):
    total += grid.step()
print(f"{grid}")
print(f"(Part 1) Total Flashes: {total}")
