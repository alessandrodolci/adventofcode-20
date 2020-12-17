import os

def get_value_range(value_range_string):
    tokens = value_range_string.split('-')
    return (int(tokens[0]), int(tokens[1]))

def is_value_valid(value, available_fields):
    for field in available_fields.values():
        for value_range_string in field:
            value_range = get_value_range(value_range_string)
            if value >= value_range[0] and value <= value_range[1]:
                return True
    
    return False

def get_scanning_error_rate(tickets, available_fields):
    invalid_values = []
    for ticket in nearby_tickets:
        for value in ticket:
            if not is_value_valid(value, available_fields):
                invalid_values.append(value)

    return sum(invalid_values)

def is_value_in_field(value, range_strings):
    for range_string in range_strings:
        value_range = get_value_range(range_string)
        if value >= value_range[0] and value <= value_range[1]:
            return True
    
    return False

def get_fields_indexes(nearby_tickets, available_fields):

    def get_next_field(fields_indexes):
        for field, indexes in fields_indexes.items():
            if len(indexes) == 1:
                return (field, indexes[0])

    fields_indexes = {}
    for field, range_strings in available_fields.items():
        fields_indexes[field] = []
        for i in range(len(nearby_tickets[0])):
            current_index_values = [ticket[i] for ticket in nearby_tickets]
            valid = True
            for value in current_index_values:
                if not is_value_in_field(value, range_strings):
                    valid = False
                    break
            if valid:
                fields_indexes[field].append(i)

    result = {}
    while len(fields_indexes.keys()) > 0:
        field, index = get_next_field(fields_indexes)
        result[field] = index
        fields_indexes.pop(field)
        for field, indexes in fields_indexes.items():
            if index in indexes:
                indexes.remove(index)

    return result

def get_valid_tickets(nearby_tickets, available_fields):
    result = []

    for ticket in nearby_tickets:
        valid = True
        for value in ticket:
            if not is_value_valid(value, available_fields):
                valid = False
                break
        if valid:
            result.append(ticket)
    
    return result

def get_departure_values_product(my_ticket, nearby_tickets, available_fields):
    product = 1
    valid_nearby_tickets = get_valid_tickets(nearby_tickets, available_fields)
    fields_indexes = get_fields_indexes(valid_nearby_tickets, available_fields)
    for field, range_strings in available_fields.items():
        if "departure" in field:
            index = fields_indexes[field]
            product *= my_ticket[index]
    
    return product

lines = []
with open(os.path.join("input", "input.txt"), 'r') as input_file:
    lines = input_file.readlines()

available_fields = {}
line = lines.pop(0)
while not line.isspace():
    tokens = line.split(':')
    field_name = tokens[0]
    values_list = tokens[1].strip().split(' or ')

    available_fields[field_name] = values_list
    line = lines.pop(0)

lines.pop(0)
my_ticket = list(map(int, lines.pop(0).strip().split(',')))

lines = lines[2:]
nearby_tickets = []
for line in lines:
    ticket = list(map(int, line.strip().split(',')))
    nearby_tickets.append(ticket)

scanning_error_rate = get_scanning_error_rate(nearby_tickets, available_fields)
departure_values_product = get_departure_values_product(my_ticket, nearby_tickets, available_fields)

print("The ticket scanning error rate is: " + str(scanning_error_rate))
print("The product of all the field values with the word \"departure\" is: " + str(departure_values_product))
