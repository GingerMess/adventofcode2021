

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
print(f'Position x depth: {final_position*final_depth}')
