import sys
from collections import deque


def count_single_increments(file_name='input.txt'):
    with open(file_name, mode='r', encoding="utf-8") as f:
        increases = 0
        previous = sys.maxsize
        for line in f:
            if line != '\n':
                number = int(line)
                if number > previous:
                    increases += 1
                previous = number
        return increases


def count_sliding_window_increments(file_name='input.txt'):
    total_increments = 0
    with open(file_name, mode='r', encoding="utf-8") as f:
        previous = deque([])
        for i in range(3):  # populate our previous window with the first 3 numbers
            previous.append(int(f.readline()))
        previous_window = sum(previous)
        for line in f:
            previous.append(int(line))  # add the newest number, queue size is now 4
            previous.popleft()  # remove the oldest number, queue size is now 3
            this_window = sum(previous)  # sum the queue, which now contains our new window
            if this_window > previous_window:
                total_increments += 1
            previous_window = this_window  # set previous window to this window
    return total_increments


increments = count_single_increments()
print(f"(Part 1) single increments: {increments}")


increments = count_sliding_window_increments()
print(f"(Part 2) sliding window increments: {increments}")
