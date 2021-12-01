import sys


def count_increments(file_name='input.txt'):
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


increments = count_increments()
print(f"Increments: {increments}")