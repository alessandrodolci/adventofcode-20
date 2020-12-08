import os

def decode_instruction(line):
    tokens = line.split()
    return (tokens[0], int(tokens[1]))

def execute_instruction(instruction):
    opcode = instruction[0]
    operand = instruction[1]

    if opcode == "acc":
        return operand
    elif opcode == "jmp" or opcode == "nop":
        return 0

    raise ValueError("The given instruction is not valid: " + instruction[0])

def get_next_instruction_offset(instruction):
    opcode = instruction[0]
    operand = instruction[1]

    if opcode == "acc":
        return 1
    elif opcode == "jmp":
        return operand
    elif opcode == "nop":
        return 1
    
    raise ValueError("The given instruction is not valid: " + instruction[0])

def run_until_first_repetition(instructions):
    program_counter = 0
    executed_instructions = []
    accumulator = 0

    while not program_counter in executed_instructions:
        instruction = decode_instruction(instructions[program_counter])

        accumulator += execute_instruction(instruction)
        
        executed_instructions.append(program_counter)
        program_counter += get_next_instruction_offset(instruction)
    
    return accumulator

def run_until_last_instruction(instructions):

    def replace_opcode(instruction):
        opcode = decode_instruction(instructions[replaced_index])[0]
        return instruction.replace(opcode, "nop" if opcode == "jmp" else "jmp")

    accumulator = 0
    replaced_index = 0
    last_instruction_executed = False

    while not last_instruction_executed:
        for replaced_index in range(replaced_index, len(instructions)):
            opcode = decode_instruction(instructions[replaced_index])[0]
            if (opcode == "jmp" or opcode == "nop"):
                instructions[replaced_index] = replace_opcode(instructions[replaced_index])
                break

        accumulator = 0
        program_counter = 0
        executed_instructions = []
        while not last_instruction_executed and not program_counter in executed_instructions:
            instruction = decode_instruction(instructions[program_counter])

            accumulator += execute_instruction(instruction)

            if program_counter == len(instructions) - 1:
                last_instruction_executed = True
                break
            else:
                executed_instructions.append(program_counter)
                program_counter += get_next_instruction_offset(instruction)
        
        instructions[replaced_index] = replace_opcode(instructions[replaced_index])
        replaced_index += 1

    return accumulator

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    instructions = input_file.readlines()
    
    accumulator_on_first_repetition = run_until_first_repetition(instructions)
    accumulator_after_last_instruction = run_until_last_instruction(instructions)
    
    print("The value of the accumulator on the first repeating instruction is: " + str(accumulator_on_first_repetition))
    print("The value of the accumulator after the last instruction executed: " + str(accumulator_after_last_instruction))
