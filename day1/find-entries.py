import os

def find_two_entries(lines):
    for i in range(0, len(lines)):
        first_entry = int(lines[i])

        for j in range(i+1, len(lines)):
            second_entry = int(lines[j])

            if first_entry + second_entry == 2020:
                return [first_entry, second_entry]
    
    return []

def find_three_entries(lines):
    for i in range(0, len(lines)):
        first_entry = int(lines[i])

        for j in range(i+1, len(lines)):
            second_entry = int(lines[j])

            for k in range(j+1, len(lines)):
                third_entry = int(lines[k])
                
                if first_entry + second_entry + third_entry == 2020:
                    return [first_entry, second_entry, third_entry]
    
    return []

def print_entries(entries):
    if len(entries) == 0:
        print("Entries not found")

    result = 1
    for entry in entries:
        result *= entry

    print("Entries found: " + ", ".join(map(str, entries)))
    print("The answer is: " + str(result))

with open(os.path.join("input", "input.txt"), "r") as input_file:
    lines = input_file.readlines()

    entries = find_two_entries(lines)
    print_entries(entries)
    
    entries = find_three_entries(lines)
    print_entries(entries)
