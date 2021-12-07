import itertools
from multiprocessing import Pool

import common


def min_fuel_constant_cost(numbers):
    median = common.average_median(numbers)
    total_fuel = sum([abs(num - median) for num in numbers])
    return total_fuel


def fuel_for_position_increasing_cost(candidate_position, numbers):
    distances = [abs(num - candidate_position) for num in numbers]
    total_fuel = sum([fuel_for_distance_increasing_cost(distance) for distance in distances])
    return total_fuel


def fuel_for_distance_increasing_cost(distance):
    # https://math.stackexchange.com/questions/1908152/how-to-calculate-the-sum-of-an-incremental-string-of-numbers
    return (distance * (distance + 1)) / 2


def min_fuel_increasing_cost(numbers):
    # brute force this by calculating fuel cost for each candidate position and picking the minimum
    minval = min(numbers)
    maxval = max(numbers)
    print(f"Zipping tuples for data range..")
    tuples = zip(range(minval, maxval + 1), itertools.repeat(numbers))
    print(f"Creating thread pool..")
    with Pool() as pool:
        print(f"Starting fuel calculations..")
        results = pool.starmap(fuel_for_position_increasing_cost, tuples)
    return min(results)


if __name__ == '__main__':
    data = common.read_all_data("input/day7.txt")
    data = [int(num) for num in ''.join(data).split(',')]
    fuel = min_fuel_constant_cost(data)
    fuel_int = int(fuel)
    print(f"(Part 1) Minimum Fuel: {fuel_int} (from {fuel})")

    fuel_part2 = min_fuel_increasing_cost(data)
    fuel_part2_int = round(fuel_part2)
    print(f"(Part 2) Minimum Fuel: {fuel_part2_int} (from {fuel_part2})")
