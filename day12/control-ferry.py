import os

EAST = 'E'
SOUTH = 'S'
WEST = 'W'
NORTH = 'N'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'
directions = [EAST, SOUTH, WEST, NORTH]

def parse_instruction(line):
    action = line[0]
    value = int(line[1:])

    return (action, value)

def move_towards_direction(current_position, direction, value):
    if direction == EAST:
        return (current_position[0] + value, current_position[1])
    elif direction == WEST:
        return (current_position[0] - value, current_position[1])
    elif direction == NORTH:
        return (current_position[0], current_position[1] + value)
    elif direction == SOUTH:
        return (current_position[0], current_position[1] - value)
    
    raise ValueError("Direction value not valid: " + direction)

def get_new_direction(current_direction, instruction):
    index_offset = (instruction[1] // 90) * (-1 if instruction[0] == LEFT else 1)
    new_direction_index = (directions.index(current_direction) + index_offset) % len(directions)
    return directions[new_direction_index]

def get_new_position(current_position, current_direction, instruction):
    action = instruction[0]
    value = instruction[1]

    if action == EAST or action == SOUTH or action == WEST or action == NORTH:
        return move_towards_direction(current_position, action, value)
    elif action == FORWARD:
        return move_towards_direction(current_position, current_direction, value)
    
    raise ValueError("Action value not valid: " + action)

def rotate_waypoint(waypoint, instruction):
    action = instruction[0]
    value = instruction[1]

    rotation = (value // 90) % 4

    if (action == LEFT and rotation == 1) or (action == RIGHT and rotation == 3):
        return (-waypoint[1], waypoint[0])
    if (action == LEFT and rotation == 3) or (action == RIGHT and rotation == 1):
        return (waypoint[1], -waypoint[0])
    if rotation == 2:
        return (-waypoint[0], -waypoint[1])
    
    raise("Rotation parameters not valid")

def get_manatthan_distance_with_wrong_actions(lines):
    position = (0, 0)
    direction = EAST

    for line in lines:
        instruction = parse_instruction(line.strip())

        if instruction[0] == LEFT or instruction[0] == RIGHT:
            direction = get_new_direction(direction, instruction)
        else:
            position = get_new_position(position, direction, instruction)
    
    return abs(position[0]) + abs(position[1])

def get_manatthan_distance_with_correct_actions(lines):
    waypoint = (10, 1)
    position = (0, 0)

    for line in lines:
        action, value = parse_instruction(line.strip())

        if action == LEFT or action == RIGHT:
            waypoint = rotate_waypoint(waypoint, (action, value))
        elif action == EAST or action == SOUTH or action == WEST or action == NORTH:
            waypoint = move_towards_direction(waypoint, action, value)
        elif action == FORWARD:
            position = (position[0] + value * waypoint[0], position[1] + value * waypoint[1])
    
    return abs(position[0]) + abs(position[1])

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    lines = input_file.readlines()

manhattan_distance = get_manatthan_distance_with_correct_actions(lines)

print("The Manhattan distance between the current location and the starting position is: " + str(manhattan_distance))
