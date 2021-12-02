def calculate_position_depth(file_name):
    position, depth = 0, 0
    with open(file_name) as file_handle:
        for line in file_handle:
            if line.startswith('forward'):
                position += int(line[8:])
            if line.startswith('down'):
                depth += int(line[5:])
            if line.startswith('up'):
                depth -= int(line[3:])
    return position, depth


final_position, final_depth = calculate_position_depth("input.txt")
print(f'Position x depth (part 1): {final_position*final_depth}')


def calculate_position_depth_aim(file_name):
    position, depth, aim = 0, 0, 0
    with open(file_name) as file_handle:
        for line in file_handle:
            if line.startswith('forward'):
                value = int(line[8:])
                position += value
                depth += (aim * value)
            if line.startswith('down'):
                aim += int(line[5:])
            if line.startswith('up'):
                aim -= int(line[3:])
    return position, depth, aim


final_position, final_depth, final_aim = calculate_position_depth_aim("input.txt")
print(f'Position x depth (part 2): {final_position * final_depth}')
