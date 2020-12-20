import os

def compute_operation(first_operand, second_operand, operator):
    if operator == '+':
        return first_operand + second_operand
    elif operator == '*':
        return first_operand * second_operand
    
    raise ValueError("Operator not valid")

def compute_sub_expression_with_precedence(operands, operators):
    while len(operands) > 1:
        i = 0
        if '+' in operators:
            i = operators.index('+')

        first_operand = operands.pop(i)
        second_operand = operands.pop(i)
        operator = operators.pop(i)
        operands.insert(i, compute_operation(first_operand, second_operand, operator))

    return operands.pop()

def compute_sub_expression(operands, operators):
    while len(operands) > 1:
        first_operand = operands.pop(0)
        second_operand = operands.pop(0)
        operator = operators.pop(0)
        operands.insert(0, compute_operation(first_operand, second_operand, operator))

    return operands.pop()

def evaluate_expression(expression):
    operands = []
    operators = []
    while expression:
        current_element = expression.pop(0)
        if current_element == '+' or current_element == '*':
            operators.append(current_element)
        elif current_element.isnumeric():
            operands.append(int(current_element))
        elif current_element == '(':
            operands.append(current_element)
        elif current_element == ')':
            inner_operands = []
            inner_operators = []
            operand = operands.pop()
            inner_operands.insert(0, operand)
            while operand != '(':
                operand = operands.pop()
                if operand != '(':
                    inner_operands.insert(0, operand)
                    operator = operators.pop()
                    inner_operators.insert(0, operator)
            
            operands.append(compute_sub_expression_with_precedence(inner_operands, inner_operators))
    
    return compute_sub_expression_with_precedence(operands, operators)

def get_sum_of_results(expressions):
    result = 0

    for expression in expressions:
        result += evaluate_expression(expression)
    
    return result

expressions = []
with open(os.path.join("input", "input.txt"), 'r') as input_file:
    for line in input_file:
        expression = line.strip().replace('(', '( ').replace(')', ' )').split()
        expressions.append(expression)

results_sum = get_sum_of_results(expressions)

print("The sum of all the expressions results is: " + str(results_sum))
