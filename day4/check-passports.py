import os, re

def parse_line(line):
    fields = line.split()

    line_fields = {}
    for field in fields:
        line_fields[field.split(':')[0]] = field.split(':')[1]

    return line_fields

def is_passport_valid(passport):
    def check_year(year, lower_bound, upper_bound):
        return len(year) == 4 and int(year) >= lower_bound and int(year) <= upper_bound
    
    if not all(field in current_passport.keys() for field in required_fields):
        return False

    birth_year = passport["byr"]
    if not check_year(birth_year, 1920, 2002):
        return False

    issue_year = passport["iyr"]
    if not check_year(issue_year, 2010, 2020):
        return False

    expiration_year = passport["eyr"]
    if not check_year(expiration_year, 2020, 2030):
        return False

    height = passport["hgt"]
    if not re.match(r"^([0-9]{3}cm|[0-9]{2}in)$", height):
        return False
    if "cm" in height:
        height_value = int(height[0:3])
        if not height_value >= 150 and height_value <= 193:
            return False
    elif "in" in height:
        height_value = int(height[0:2])
        if not height_value >= 59 and height_value <= 76:
            return False

    hair_color = passport["hcl"]
    if not re.match(r"^#[0-9a-f]{6}$", hair_color):
        return False

    eye_color = passport["ecl"]
    if not re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", eye_color):
        return False

    passport_id = passport["pid"]
    if not re.match(r"^[0-9]{9}$", passport_id):
        return False

    return True

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open(os.path.join("input", "input.txt"), "r") as input_file:
    valid_passports_count = 0

    current_passport = {}
    for line in input_file:
        if line.isspace():
            if is_passport_valid(current_passport):
                valid_passports_count += 1
            current_passport.clear()
        else:
            current_passport.update(parse_line(line))
    if is_passport_valid(current_passport):
        valid_passports_count += 1
    
    print("The number of valid passports is: " + str(valid_passports_count))
