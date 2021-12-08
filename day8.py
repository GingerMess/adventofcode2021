import collections

import common


def contains_all_segments(first, second):
    # return true if first contains all segments in second
    return set(first).issuperset(set(second))


def common_segments(pattern1, pattern2):
    # return the common segments between two patterns
    return set(pattern1).intersection(set(pattern2))


# this function only works for part 2!
def digits_for_patterns(patterns_orig):
    patterns = patterns_orig.copy()
    # sort the segments in each pattern alphabetically, so the comparisons are normalised
    patterns = [''.join(sorted(pattern)) for pattern in patterns]
    digit_to_pattern_map = dict()
    # determine the obvious ones based on unique segment counts
    digit_to_pattern_map[1] = next(pattern for pattern in patterns if len(pattern) == 2)
    digit_to_pattern_map[7] = next(pattern for pattern in patterns if len(pattern) == 3)
    digit_to_pattern_map[4] = next(pattern for pattern in patterns if len(pattern) == 4)
    digit_to_pattern_map[8] = next(pattern for pattern in patterns if len(pattern) == 7)
    for key in [1, 7, 8, 4]:
        patterns.remove(digit_to_pattern_map[key])
    length_5_patterns = [pattern for pattern in patterns if len(pattern) == 5]
    length_6_patterns = [pattern for pattern in patterns if len(pattern) == 6]
    # find 9 (pattern of length 6 that contains all segments in 4's pattern)
    digit_to_pattern_map[9] = next(pattern for pattern in length_6_patterns if contains_all_segments(pattern, digit_to_pattern_map[4]))
    length_6_patterns.remove(digit_to_pattern_map[9])
    # find 0 (pattern of length 6 that contains all segments in 1's pattern)
    digit_to_pattern_map[0] = next(pattern for pattern in length_6_patterns if contains_all_segments(pattern, digit_to_pattern_map[1]))
    length_6_patterns.remove(digit_to_pattern_map[0])
    # find 6 (last remaining length 6 pattern)
    digit_to_pattern_map[6] = length_6_patterns[0]
    # find 3 (pattern of length 5 that contains all segments in 7's pattern)
    digit_to_pattern_map[3] = next(pattern for pattern in length_5_patterns if contains_all_segments(pattern, digit_to_pattern_map[7]))
    length_5_patterns.remove(digit_to_pattern_map[3])
    # find 2 (pattern of length 5 that does *not* contain the single common segment between 1 and 6)
    # finding 5 is simply the remaining length 5 pattern after 2
    common_segs = list(common_segments(digit_to_pattern_map[1], digit_to_pattern_map[6]))
    for pattern in length_5_patterns:
        if common_segs[0] in set(pattern):  # we know we only have 1 common segment between 1 and 6
            digit_to_pattern_map[5] = pattern
            length_5_patterns.remove(pattern)
            digit_to_pattern_map[2] = length_5_patterns[0]
    return digit_to_pattern_map


data = common.read_all_data("input/day8.txt")
digits_by_count = collections.defaultdict(lambda: 0)
for line in data:
    tokens = line.split('|')
    signal_patterns = tokens[0].strip().split(' ')
    output_values = tokens[1].strip().split(' ')
    digits_by_count[1] += len([pattern for pattern in output_values if len(pattern) == 2])
    digits_by_count[7] += len([pattern for pattern in output_values if len(pattern) == 3])
    digits_by_count[4] += len([pattern for pattern in output_values if len(pattern) == 4])
    digits_by_count[8] += len([pattern for pattern in output_values if len(pattern) == 7])
print(f"(Part 1) Total count: {sum([pair[1] for pair in digits_by_count.items()])}")

total = 0
for line in data:
    tokens = line.split('|')
    signal_patterns = tokens[0].strip().split(' ')
    output_values = tokens[1].strip().split(' ')
    # determine mapping
    digits_to_patterns = digits_for_patterns(signal_patterns)
    # decode the output
    decoded_digits_as_str = ''
    for output_value in output_values:
        sorted_output_value = ''.join(sorted(output_value))
        digit = next(pair[0] for pair in digits_to_patterns.items() if pair[1] == sorted_output_value)
        decoded_digits_as_str += str(digit)
    total += int(decoded_digits_as_str)
print(f"(Part 2) Total of all output values: {total}")
