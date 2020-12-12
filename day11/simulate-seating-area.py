import os, copy

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

def count_occupied_seats(area):
    result = 0
    
    for row in area:
        for seat in row:
            if seat == OCCUPIED:
                result += 1
    
    return result

# This one screams for refactoring
def get_adjacent_seats(area, row_index, column_index, distance = -1):
    result = []

    i = row_index
    j = column_index
    current_seat = FLOOR
    steps = 0
    while i != 1 and (distance == -1 or steps < distance) and current_seat != EMPTY and current_seat != OCCUPIED:
        current_seat = area[i-1][j]
        if current_seat == EMPTY or current_seat == OCCUPIED:
            result.append(current_seat)
        i -= 1
        steps += 1
    
    i = row_index
    j = column_index
    current_seat = FLOOR
    steps = 0
    while i != len(area) - 2 and (distance == -1 or steps < distance) and current_seat != EMPTY and current_seat != OCCUPIED:
        current_seat = area[i+1][j]
        if current_seat == EMPTY or current_seat == OCCUPIED:
            result.append(current_seat)
        i += 1
        steps += 1
    
    i = row_index
    j = column_index
    current_seat = FLOOR
    steps = 0
    while j != 1 and (distance == -1 or steps < distance) and current_seat != EMPTY and current_seat != OCCUPIED:
        current_seat = area[i][j-1]
        if current_seat == EMPTY or current_seat == OCCUPIED:
            result.append(current_seat)
        j -= 1
        steps += 1
    
    i = row_index
    j = column_index
    current_seat = FLOOR
    steps = 0
    while j != len(area[0]) - 2 and (distance == -1 or steps < distance) and current_seat != EMPTY and current_seat != OCCUPIED:
        current_seat = area[i][j+1]
        if current_seat == EMPTY or current_seat == OCCUPIED:
            result.append(current_seat)
        j += 1
        steps += 1
    
    i = row_index
    j = column_index
    current_seat = FLOOR
    steps = 0
    while i != 1 and j != 1 and (distance == -1 or steps < distance) and  current_seat != EMPTY and current_seat != OCCUPIED:
        current_seat = area[i-1][j-1]
        if current_seat == EMPTY or current_seat == OCCUPIED:
            result.append(current_seat)
        i -= 1
        j -= 1
        steps += 1
    
    i = row_index
    j = column_index
    current_seat = FLOOR
    steps = 0
    while i != 1 and j != len(area[0]) - 2 and (distance == -1 or steps < distance) and current_seat != EMPTY and current_seat != OCCUPIED:
        current_seat = area[i-1][j+1]
        if current_seat == EMPTY or current_seat == OCCUPIED:
            result.append(current_seat)
        i -= 1
        j += 1
        steps += 1
    
    i = row_index
    j = column_index
    current_seat = FLOOR
    steps = 0
    while i != len(area) - 2 and j != len(area[0]) - 2 and (distance == -1 or steps < distance) and current_seat != EMPTY and current_seat != OCCUPIED:
        current_seat = area[i+1][j+1]
        if current_seat == EMPTY or current_seat == OCCUPIED:
            result.append(current_seat)
        i += 1
        j += 1
        steps += 1
    
    i = row_index
    j = column_index
    current_seat = FLOOR
    steps = 0
    while i != len(area) - 2 and j != 1 and (distance == -1 or steps < distance) and current_seat != EMPTY and current_seat != OCCUPIED:
        current_seat = area[i+1][j-1]
        if current_seat == EMPTY or current_seat == OCCUPIED:
            result.append(current_seat)
        i += 1
        j -= 1
        steps += 1
    
    return result
            

def should_occupy_seat(area, row_index, column_index):
    adjacent_seats = get_adjacent_seats(area, row_index, column_index)
    for seat in adjacent_seats:
        if seat != EMPTY:
            return False
    
    return True
    
def should_empty_seat(area, row_index, column_index):
    adjacent_seats = get_adjacent_seats(area, row_index, column_index)
    occupied_adjacent_count = 0
    for seat in adjacent_seats:
        if seat == OCCUPIED:
            occupied_adjacent_count += 1
    
    return occupied_adjacent_count >= 5

def should_seat_change(area, row_index, column_index):
    if area[row_index][column_index] == EMPTY:
        return should_occupy_seat(area, row_index, column_index)
    elif area[row_index][column_index] == OCCUPIED:
        return should_empty_seat(area, row_index, column_index)
    else:
        return False

def simulate_area(area):
    changed = True
    while changed:
        changed = False

        next_area = copy.deepcopy(area)

        for i in range(1, len(area) - 1):
            for j in range(1, len(area[0])):
                if should_seat_change(area, i, j):
                    next_area[i][j] = OCCUPIED if area[i][j] == EMPTY else EMPTY
                    changed = True

        area = next_area
    
    return area

seating_area = []

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    lines = input_file.readlines()

    row_length = len(lines[0].strip()) + 2
    seating_area.append([FLOOR for i in range(row_length)])

    for line in lines:
        row = [FLOOR]
        for seat in line.strip():
            row.append(seat)
        row.append(FLOOR)
        seating_area.append(row)
    
    seating_area.append([FLOOR for i in range(row_length)])

seating_area = simulate_area(seating_area)
occupied_seats_count = count_occupied_seats(seating_area)

print("The number of occupied seats after the simulation is: " + str(occupied_seats_count))
