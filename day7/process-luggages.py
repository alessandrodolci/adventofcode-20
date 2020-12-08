import os

def get_containing_bag(line):
    return line.split("bags")[0].strip()

def get_contained_bags(line):
    result = []
    
    tokens = line.split("bag")
    for token in tokens[1:-1]:
        count = token.split()[-3]
        bag = ' '.join(token.split()[-2:])
        if count.isdigit():
            result.append((bag, int(count)))
    
    return result

def get_container_bags_count(bags_to_containers, current_containers, container_index, bags_count):
    if container_index == len(current_containers):
        return bags_count
    
    current_bag = current_containers[container_index]
    new_containers = bags_to_containers.get(current_bag)
    if new_containers:
        for bag in new_containers:
            if bag not in current_containers:
                current_containers.append(bag)
                bags_count += 1

    return get_container_bags_count(bags_to_containers, current_containers, container_index + 1, bags_count)

def get_contained_bags_count(bags_to_contained, current_contained, contained_index, bags_count):
    if contained_index == len(current_contained):
        return bags_count

    current_bag = current_contained[contained_index][0]
    current_count = current_contained[contained_index][1]
    new_contained = bags_to_contained.get(current_bag)
    if new_contained:
        for bag in new_contained:
            current_contained.append((bag[0], current_count * bag[1]))
    bags_count += current_count

    return get_contained_bags_count(bags_to_contained, current_contained, contained_index + 1, bags_count)

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    bags_to_contained = {}
    bags_to_containers = {}
    for line in input_file:
        containing_bag = get_containing_bag(line)
        contained_bags = get_contained_bags(line)

        bags_to_contained[containing_bag] = contained_bags

        for bag in contained_bags:
            bag_name = bag[0]
            containing_list = bags_to_containers.get(bag_name, [])
            containing_list.append(containing_bag)
            bags_to_containers[bag_name] = containing_list

    bags_containing_gold = bags_to_containers["shiny gold"]
    container_bags_count = get_container_bags_count(bags_to_containers, bags_containing_gold, 0, len(bags_containing_gold))

    bags_contained_in_gold = bags_to_contained["shiny gold"]
    contained_bags_count = get_contained_bags_count(bags_to_contained, bags_contained_in_gold, 0, 0)
    
    print("The number of possible containers for shiny gold bags is: " + str(container_bags_count))
    print("The number of bags contained in a shiny gold bag is: " + str(contained_bags_count))
