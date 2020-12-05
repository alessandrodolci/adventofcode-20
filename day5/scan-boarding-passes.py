import os, bisect

def find_index(string, low_char, up_char, upper_bound):
    index = 0
    current_upper_bound = upper_bound

    for instruction in string:
        if instruction == low_char:
            current_upper_bound = (current_upper_bound + index) // 2
        elif instruction == up_char:
            index = (current_upper_bound + index) // 2 + 1
    
    return index

def get_seat_position(boarding_pass):
    row_string = boarding_pass[0:7]
    column_string = boarding_pass[7:10]

    row_number = find_index(row_string, 'F', 'B', 127)
    column_number = find_index(column_string, 'L', 'R', 7)
    
    return (row_number, column_number)

def get_my_seat(ordered_seats):
    for i in range(1, len(ordered_seats) - 1):
        if ordered_seats[i] == ordered_seats[i-1] + 2:
            return ordered_seats[i] - 1

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    seats = []

    for line in input_file:
        seat = get_seat_position(line)
        bisect.insort(seats, seat[0] * 8 + seat[1])
    
    my_seat_id = get_my_seat(seats)

    print("The highest seat ID found is: " + str(max(seats)))
    print("My seat ID is: " + str(my_seat_id))
