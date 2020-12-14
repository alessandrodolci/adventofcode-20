import os

def get_sum_first_version(lines):
    memory = {}
    mask = ""
    for line in lines:
        tokens = line.strip().split()
        lvalue = tokens[0]
        if lvalue == "mask":
            mask = tokens[2]
        else:
            address = lvalue.replace("mem[", '').replace(']', '')
            value = int(tokens[2])

            bit_value = list(format(value, "036b"))
            for i, bit in enumerate(mask):
                if bit == '0' or bit == '1':
                    bit_value[i] = bit
            bit_value = ''.join(bit_value)

            memory[address] = int(bit_value, 2)
    
    return sum(memory.values())

def get_sum_second_version(lines):

    def replace_floating_bit(address, i):
        address = list(address)

        first_address = address.copy()
        second_address = address.copy()
        first_address[i] = '0'
        second_address[i] = '1'

        return [''.join(first_address), ''.join(second_address)]

    memory = {}
    mask = ""
    for line in lines:
        tokens = line.strip().split()
        lvalue = tokens[0]
        if lvalue == "mask":
            mask = tokens[2]
        else:
            address = int(lvalue.replace("mem[", '').replace(']', ''))
            value = int(tokens[2])

            final_bit_value = list(format(address, "036b"))
            for i, bit in enumerate(mask):
                if bit == '1' or bit == 'X':
                    final_bit_value[i] = bit
            addresses = [''.join(final_bit_value)]

            for i, bit in enumerate(final_bit_value):
                if bit == 'X':
                    new_addresses = []
                    for address in addresses:
                        new_addresses.extend(replace_floating_bit(address, i))
                    addresses = new_addresses

            for address in addresses:
                address = int(address, 2)
                memory[address] = value
    
    return sum(memory.values())

lines = []
with open(os.path.join("input", "input.txt"), 'r') as input_file:
    lines = input_file.readlines()

result_first_version = get_sum_first_version(lines)
result_second_version = get_sum_second_version(lines)

print("The sum of all values in memory after the initialization with the v1 decoder is: ", result_first_version)
print("The sum of all values in memory after the initialization with the v2 decoder is: ", result_second_version)
