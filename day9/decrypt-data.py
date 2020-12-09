import os

def get_invalid_number(numbers):
    for i in range(25, len(numbers)):
        number = numbers[i]

        found = False
        for j in range(i - 25, i):
            for k in range(i - 25, i):
                if k != j and number == numbers[k] + numbers[j]:
                    found = True
                    break
            if found:
                break

        if not found:
            return number
    
    return -1

def get_contiguous_range(numbers, invalid_number):
    for i, number in enumerate(numbers):
        contiguous_range = [number]

        j = i + 1
        while sum(contiguous_range) < invalid_number:
            contiguous_range.append(numbers[j])

            if sum(contiguous_range) != invalid_number:
                j += 1

        if sum(contiguous_range) == invalid_number:
            return contiguous_range

    return []

numbers = []

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    for line in input_file:
        numbers.append(int(line))

invalid_number = get_invalid_number(numbers)
contiguous_range = get_contiguous_range(numbers, invalid_number)
encryption_weakness = min(contiguous_range) + max(contiguous_range)

print("The first number that is not the sum of any of the previous 25 numbers is: " + str(invalid_number))
print("The encryption weakness is: " + str(encryption_weakness))
