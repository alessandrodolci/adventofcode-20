import os

def count_trees(lines, steps_right, steps_down):
    trees = 0
    x_index = 0
    y_index = 0

    while y_index < len(lines):
        line = lines[y_index]

        if line[x_index] == '#':
            trees += 1
        
        x_index = (x_index + steps_right) % len(line)
        y_index += steps_down
    
    return trees

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    lines = input_file.read().splitlines()

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for (x, y) in slopes:
        tree_count = count_trees(lines, x, y)
        print("The tree count for slope (" + str(x) + ", " + str(y) + ") is: " + str(tree_count))

        result *= tree_count

    print("The final result is: " + str(result))
