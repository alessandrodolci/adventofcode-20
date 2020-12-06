import os

def get_sum_with_anyone_answers(lines):
    result = 0
    current_group_questions = set()

    for line in lines:
        if line.isspace():
            result += len(current_group_questions)
            current_group_questions.clear()
        else:
            for question in line.strip():
                current_group_questions.add(question)
    result += len(current_group_questions)

    return result

def get_sum_with_everyone_answers(lines):
    result = 0

    current_group_questions = set()
    begin_group = True
    for line in lines:
        if line.isspace():
            result += len(current_group_questions)
            current_group_questions.clear()
            begin_group = True
        else:
            if begin_group == True:
                for question in line.strip():
                    current_group_questions.add(question)
                begin_group = False
            else:
                current_group_questions = current_group_questions.intersection(set(line))
    result += len(current_group_questions)

    return result

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    lines = input_file.readlines()
    total_sum = get_sum_with_everyone_answers(lines)

    print("The total sum of every group's positive answered question is " + str(total_sum))
