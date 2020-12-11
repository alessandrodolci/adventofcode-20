import os

def get_jolt_differences(adapters, difference):
    result = 0
    
    current_adapter = adapters[0]
    for adapter in adapters:
        if adapter - current_adapter == difference:
            result += 1
        current_adapter = adapter
    
    return result

def get_possible_arrangements_count(adapters):
    
    def are_adapters_compatible(first, second):
        return second - first >= 0 and second - first <= 3

    def get_possible_next_indexes(current_index):
        result = []
        if current_index + 1 < len(adapters):
            result.append(current_index + 1)
        if current_index + 2 < len(adapters) and are_adapters_compatible(adapters[current_index], adapters[current_index+2]):
            result.append(current_index + 2)
        if current_index + 3 < len(adapters) and are_adapters_compatible(adapters[current_index], adapters[current_index+3]):
            result.append(current_index + 3)
        
        return result

    # I admit I had to look up on function memoization,
    # anyway, still not proud of this brute-force approach
    use_adapter_results = {}
    def use_adapter(index):
        if index in use_adapter_results.keys():
            return use_adapter_results[index]

        possible_next_indexes = get_possible_next_indexes(index)
        
        if len(possible_next_indexes) == 0:
            result = 1
            use_adapter_results[index] = result
            return result
        else:
            result = sum(use_adapter(next_index) for next_index in possible_next_indexes)
            use_adapter_results[index] = result
            return result
    
    return use_adapter(0)

adapters = [0]

with open(os.path.join("input", "input.txt"), 'r') as input_file:
    for line in input_file:
        adapters.append(int(line))

built_in_adapter = max(adapters) + 3
adapters.append(built_in_adapter)

adapters.sort()

one_jolt_differences = get_jolt_differences(adapters, 1)
three_jolt_differences = get_jolt_differences(adapters, 3)

possible_arrangements_count = get_possible_arrangements_count(adapters)

print("The product of one-jolt and three-jolt differences is: ", str(one_jolt_differences * three_jolt_differences))
print("The number of possible arrangements is: " + str(possible_arrangements_count))
