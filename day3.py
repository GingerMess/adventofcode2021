def most_common_bits(values, preferred='1'):
    # init our counter lists
    ones = [0] * 12
    zeroes = [0] * 12
    for line in values:
        for i in range(len(line)):
            if line[i] == '0':
                zeroes[i] += 1
            if line[i] == '1':
                ones[i] += 1
    # determine whether ones outnumber zeroes for each index
    result = ""
    for i in range(len(ones)):
        if ones[i] > zeroes[i]:
            result += '1'
        elif ones[i] < zeroes[i]:
            result += '0'
        else:
            result += preferred
    return result


def matches_bit(value, position, expected_bit):
    return value[position] == expected_bit


def read_all_data(file_name):
    with open(file_name) as f:
        return list(line.strip() for line in f)

# part 1 - gamma and epsilon
original_data = read_all_data("input/day3.txt")
most_common = most_common_bits(original_data, '1')
least_common = ''.join('1' if char == '0' else '0' for char in most_common)  # bitwise inverse (man i hate python sometimes)
gamma = int(most_common, 2)
epsilon = int(least_common, 2)
print(f"Gamma * Epsilon: {gamma * epsilon}")

# part 2 - oxygen
filtered = original_data.copy()
offset = 0
while len(filtered) > 1:
    filtered = [line for line in filtered if matches_bit(line, offset, most_common[offset])]
    most_common = most_common_bits(filtered, '1')  # recalculate common bits - the challenge wasn't amazingly well written so i missed this requirement
    offset += 1
oxygen = int(filtered[0], 2)

# part 2 - scrubber
# least common with 0 preference, negated, equals most common with 1 preference
least_common = ''.join('1' if char == '0' else '0' for char in most_common_bits(original_data, '1'))
filtered = original_data.copy()
offset = 0
while len(filtered) > 1:
    filtered = [line for line in filtered if matches_bit(line, offset, least_common[offset])]
    least_common = ''.join('1' if char == '0' else '0' for char in most_common_bits(filtered, '1'))
    offset += 1
scrubber = int(filtered[0], 2)

lifesupport = oxygen * scrubber
print(f"Life Support: {lifesupport}")
