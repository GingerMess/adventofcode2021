def most_common_bits(file_name):
    # init our counter lists
    ones = [0] * 12
    zeroes = [0] * 12
    with open(file_name) as f:
        for line in f:
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
        else:
            result += '0'
    return result


most_common = most_common_bits("input.txt")
# gamma is the most common, so just convert direct to int
gamma = int(most_common, 2)
# epsilon is the inverse, no easy way to do this in python?
epsilon = int(''.join('0' if char == '1' else '1' for char in most_common), 2)
print(f"Gamma * Epsilon: {gamma * epsilon}")
