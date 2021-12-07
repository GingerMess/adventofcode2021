import common


def calculate_minimum_fuel(numbers):
    median = common.average_median(numbers)
    total_fuel = sum([abs(num - median) for num in numbers])
    return total_fuel


data = common.read_all_data("input/day7.txt")
data = [int(num) for num in ''.join(data).split(',')]
fuel = calculate_minimum_fuel(data)
fuel_int = int(fuel)
print(f"(Part 1) Minimum Fuel: {fuel_int} (from {fuel})")
