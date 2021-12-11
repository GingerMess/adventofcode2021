from math import floor

import common


def calculate_syntax_error(lines):
    corrupted_total = 0
    repair_scores = []
    for line in lines:
        stack = []
        corrupted = 0
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
        corrupted_total += corrupted
        if corrupted > 0:
            continue
        if len(stack) > 0:
            # line is incomplete
            matching_brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
            repair_string = list(reversed([matching_brackets[opener] for opener in stack]))
            scores = {')': 1, ']': 2, '}': 3, '>': 4}
            score = 0
            for char in repair_string:
                score = (score * 5) + (scores[char])
            repair_scores.append(score)
    return corrupted_total, repair_scores


data = common.read_all_data("input/day10.txt")
corruption, repairs = calculate_syntax_error(data)
sorted_repairs = sorted(repairs)
middle_score = sorted_repairs[floor(len(sorted_repairs) / 2)]
print(f"(Part 1) Total Syntax Error: {corruption}")
print(f"(Part 2) Middle Repair Score: {middle_score}")
