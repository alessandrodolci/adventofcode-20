import os

def find_earliest_bus(earliest_timestamp, schedules):

    def get_minutes_to_wait(bus_id):
        return bus_id - earliest_timestamp % bus_id

    if len(schedules) == 0:
        raise ValueError("Empty schedules list")

    bus_id = schedules[0]
    minutes_to_wait = get_minutes_to_wait(bus_id)
    for current_bus_id in schedules[1:]:
        current_minutes_to_wait = get_minutes_to_wait(current_bus_id)
        if current_minutes_to_wait < minutes_to_wait:
            bus_id = current_bus_id
            minutes_to_wait = current_minutes_to_wait
    
    return (bus_id, minutes_to_wait)

def find_special_timestamp(schedules):
    if len(schedules) == 0:
        raise ValueError("Empty schedules list")

    initial_timestamp = int(schedules[0])
    i = 0
    found = False
    while found == False:
        i += 1
        found = True
        for j, bus_id_string in enumerate(schedules[1:]):
            try:
                bus_id = int(bus_id_string)
                if ((initial_timestamp * i) + j + 1) % bus_id != 0:
                    found = False
                    break
            except (ValueError):
                continue

    return initial_timestamp * i

lines = []
with open(os.path.join("input", "input.txt"), 'r') as input_file:
    lines = input_file.readlines()

earliest_timestamp = int(lines[0].strip())
filtered_schedules = list(map(int, lines[1].strip().replace('x,', '').split(',')))
complete_schedules = lines[1].strip().split(',')

bus_id, minutes_to_wait = find_earliest_bus(earliest_timestamp, filtered_schedules)
special_timestamp = find_special_timestamp(complete_schedules)

print("The ID of the earliest available bus is: " + str(bus_id) + ", the result is: " + str(bus_id * minutes_to_wait))
print("The first timestamp such that all buses depart at their specific offset after it is: " + str(special_timestamp))
