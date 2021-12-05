import os
import sys


def read_all_data(file_name):
    with open(os.path.join(sys.path[0], file_name)) as f:
        return list(line.strip() for line in f)


def flatmap(lists):
    return [element for sublist in lists for element in sublist]
