import sys
from collections import deque


def count_single_increments(file_name='input/day1.txt'):
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


def count_sliding_window_increments(file_name='input/day1.txt'):
    increases = 0
    with open(file_name, mode='r', encoding="utf-8") as f:
        queue = deque([])
        for i in range(3):  # populate our queue with the first 3 numbers
            queue.append(int(f.readline()))
        previous_total = sum(queue)  # sum the first 3 numbers to create our first window total
        for line in f:
            queue.append(int(line))  # add the newest number, queue size is now 4
            queue.popleft()  # remove the oldest number, queue size is now 3
            current_total = sum(queue)  # sum the queue, which now contains our current window's total
            if current_total > previous_total:
                increases += 1
            previous_total = current_total  # set previous total to this window's total
    return increases


increments = count_single_increments()
print(f"(Part 1) single increments: {increments}")


increments = count_sliding_window_increments()
print(f"(Part 2) sliding window increments: {increments}")
