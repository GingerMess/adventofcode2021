import collections

import common


def digit_for_pattern(segment_pattern):
    match len(segment_pattern):
        case 2: return 1
        case 3: return 7
        case 4: return 4
        case 7: return 8
    return None


data = common.read_all_data("input/day8.txt")
digits_by_count = collections.defaultdict(lambda: 0)
for line in data:
    tokens = line.split('|')
    signal_patterns = tokens[0].strip().split(' ')
    output_values = tokens[1].strip().split(' ')
    for pattern in output_values:
        digit = digit_for_pattern(pattern)
        if digit is not None:
            digits_by_count[digit] += 1

print(f"(Part 1) Digit counts: {digits_by_count} Total count: {sum([pair[1] for pair in digits_by_count.items()])}")
