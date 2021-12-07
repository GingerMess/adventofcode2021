import os
import sys
from math import floor


def read_all_data(file_name):
    with open(os.path.join(sys.path[0], file_name)) as f:
        return list(line.strip() for line in f)


def flatmap(lists):
    return [element for sublist in lists for element in sublist]


def average_mean(numbers):
    return sum(numbers) / len(numbers)


def average_median(numbers):
    length = len(numbers)
    sorted_numbers = sorted(numbers)
    start_index = floor(length/2)
    if is_even(len(sorted_numbers)):
        return (sorted_numbers[start_index] + sorted_numbers[start_index-1]) / 2
    else:
        return sorted_numbers[start_index]


def is_even(number):
    return number % 2 == 0

