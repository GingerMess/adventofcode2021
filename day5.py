from dataclasses import dataclass

import common


@dataclass
class Grid:
    squares: dict

    def __init__(self):
        self.squares = {}

    def apply(self, line):
        xstep = -1 if line.start.x > line.end.x else 1
        ystep = -1 if line.start.y > line.end.y else 1
        for x in range(line.start.x, line.end.x + xstep, xstep):
            for y in range(line.start.y, line.end.y + ystep, ystep):
                self.apply_point(Point(x, y))

    def apply_point(self, point):
        count = self.squares.get(point, 0)
        count += 1
        self.squares[point] = count

    def highest_count(self):
        # return Point,count pair with highest count
        highest_pair = (Point(0, 0), 0)
        for pair in self.squares.items():
            if pair[1] > highest_pair[1]:
                highest_pair = pair
        return highest_pair

    def squares_with_count_equal_or_greater(self, count):
        total = 0
        for pair in self.squares.items():
            if pair[1] >= count:
                total += 1
        return total


@dataclass
class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


@dataclass
class Line:
    start: Point(0, 0)
    end: Point(0, 0)

    def __init__(self, start, end):
        self.start = start
        self.end = end


data = common.read_all_data("input/day5.txt")
horizontal_vertical_lines = []
other_lines = []
for line in data:
    # assumes no broken data
    tokens = line.strip().split(' ')
    # split each point token into ints and unwrap the args array into the Point constructor
    start = Point(*[int(val) for val in tokens[0].split(',')])
    end = Point(*[int(val) for val in tokens[2].split(',')])
    if start.x == end.x or start.y == end.y:
        horizontal_vertical_lines.append(Line(start, end))
    else:
        other_lines.append(Line(start, end))
grid = Grid()
line_number = 1
for line in horizontal_vertical_lines:
    grid.apply(line)
    print(f"Processed h/v line {line_number}/{len(horizontal_vertical_lines)} ({line})")
    line_number += 1

print(f"Highest count: {grid.highest_count()}")
print(f"Total squares with overlap: {grid.squares_with_count_equal_or_greater(2)}")
