import common


def calculate_syntax_error(lines):
    stack = []
    corrupted_total = 0
    for line in lines:
        corrupted = 0
        incomplete = False
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
                continue
            expected_opposite = stack.pop()
            match char:
                case ')':
                    if expected_opposite != '(':
                        corrupted = 3
                        break
                case ']':
                    if expected_opposite != '[':
                        corrupted = 57
                        break
                case '}':
                    if expected_opposite != '{':
                        corrupted = 1197
                        break
                case '>':
                    if expected_opposite != '<':
                        corrupted = 25137
                        break
        if len(stack) > 0:
            incomplete = True
        corrupted_total += corrupted
    return corrupted_total


data = common.read_all_data("input/day10.txt")
syntax_error = calculate_syntax_error(data)
print(f"(Part 1) Total Syntax Error: {syntax_error}")
