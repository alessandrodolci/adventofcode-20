import os

def count_with_wrong_policy(lines):
    valid_passwords_count = 0

    for line in lines:
        fields = line.split()

        bounds = fields[0]

        lower_bound = int(bounds[0:bounds.index('-')])
        upper_bound = int(bounds[bounds.index('-')+1:len(bounds)])

        letter = fields[1][0]

        candidate = fields[2]

        letter_occurences = candidate.count(letter)
        if letter_occurences >= lower_bound and letter_occurences <= upper_bound:
            valid_passwords_count += 1
    
    return valid_passwords_count

def count_with_official_toboggan_corporate_policy(lines):
    valid_passwords_count = 0

    for line in lines:
        fields = line.split()
        
        bounds = fields[0]

        first_index = int(bounds[0:bounds.index('-')]) - 1
        second_index = int(bounds[bounds.index('-')+1:len(bounds)]) - 1

        letter = fields[1][0]

        candidate = fields[2]

        if (candidate[first_index] == letter) != (candidate[second_index] == letter):
            valid_passwords_count += 1

    return valid_passwords_count

with open(os.path.join("input", "input.txt"), "r") as input_file:
    lines = input_file.readlines()
    
    valid_passwords_count = count_with_official_toboggan_corporate_policy(lines)
    print("The number of valid passwords is: " + str(valid_passwords_count))
