import os, copy

CYCLES = 6
ACTIVE = '#'
INACTIVE = '.'

def get_active_neighbors(cubes, i, j, k):
    result = 0
    for ii in range(i-1, i+2):
        if ii in cubes:
            for jj in range(j-1, j+2):
                if jj in cubes[ii]:
                    for kk in range(k-1, k+2):
                        if kk in cubes[ii][jj] and not (ii == i and jj == j and kk == k) and cubes[ii][jj][kk] == ACTIVE:
                            result += 1
    
    return result

def get_next_cube(cubes, i, j, k):
    cube = cubes[i][j][k]
    active_neighbors = get_active_neighbors(cubes, i, j, k)
    if ((cube == ACTIVE and (active_neighbors == 2 or active_neighbors == 3))
        or (cube == INACTIVE and active_neighbors == 3)):
        return ACTIVE
    
    return INACTIVE

def pad_cubes(cubes):
    min_i = min(cubes.keys())
    cubes[min_i-1] = {}
    for j in cubes[0].keys():
        cubes[min_i-1][j] = {}
        for k in cubes[0][j].keys():
            cubes[min_i-1][j][k] = INACTIVE

    for i in cubes.keys():
        min_j = min(cubes[i].keys())
        cubes[i][min_j-1] = {}
        for k in cubes[0][0].keys():
            cubes[i][min_j-1][k] = INACTIVE
        max_j = max(cubes[i].keys())
        cubes[i][max_j+1] = {}
        for k in cubes[0][0].keys():
            cubes[i][max_j+1][k] = INACTIVE

    max_i = max(cubes.keys())
    cubes[max_i+1] = {}
    for j in cubes[0].keys():
        cubes[max_i+1][j] = {}
        for k in cubes[0][j].keys():
            cubes[max_i+1][j][k] = INACTIVE
    
    for i in cubes.keys():
        for j in cubes[i].keys():
            min_k = min(cubes[i][j].keys())
            cubes[i][j][min_k-1] = INACTIVE
            max_k = max(cubes[i][j].keys())
            cubes[i][j][max_k+1] = INACTIVE

def get_active_cubes_after_simulation(cubes):
    for cycle in range(CYCLES):
        next_cubes = copy.deepcopy(cubes)
        for i in cubes.keys():
            for j in cubes[i].keys():
                for k in cubes[i][j].keys():
                    next_cubes[i][j][k] = get_next_cube(cubes, i, j, k)

        pad_cubes(next_cubes)
        cubes = next_cubes
    
    result = 0
    for i in cubes.keys():
        for j in cubes[i].keys():
            for k in cubes[i][j].keys():
                if cubes[i][j][k] == ACTIVE:
                    result += 1
    
    return result

lines = []
with open(os.path.join("input", "input.txt"), 'r') as input_file:
    lines = [line.strip() for line in input_file]

cubes = {}
for i, line in enumerate(lines):
    cubes[i] = {}
    for j, cube in enumerate(line.strip()):
        cubes[i][j] = {}
        cubes[i][j][0] = cube

pad_cubes(cubes)
print(cubes)

active_cubes = get_active_cubes_after_simulation(cubes)

print("The number of active cubes after the simulation is: " + str(active_cubes))
