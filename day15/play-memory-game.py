import os

initial_numbers = []
with open(os.path.join("input", "input.txt"), 'r') as input_file:
    initial_numbers = list(map(int, input_file.readline().strip().split(',')))

numbers = {}
last_number_spoken = initial_numbers[0]

for i, number in enumerate(initial_numbers[1:]):
    numbers[last_number_spoken] = i + 1
    last_number_spoken = number

stop_index = 30000000
for i in range(len(initial_numbers), stop_index):
    if last_number_spoken in numbers:
        next_number = i - numbers[last_number_spoken]
        numbers[last_number_spoken] = i
        last_number_spoken = next_number
    else:
        numbers[last_number_spoken] = i
        last_number_spoken = 0

print("The " + str(stop_index) + "th number spoken is: " + str(last_number_spoken))
