import os, copy

CYCLES = 6
ACTIVE = '#'
INACTIVE = '.'

def get_active_neighbors(cubes, i, j, k, l):
    result = 0
    for ii in range(i-1, i+2):
        if ii in cubes:
            for jj in range(j-1, j+2):
                if jj in cubes[ii]:
                    for kk in range(k-1, k+2):
                        if kk in cubes[ii][jj]:
                            for ll in range(l-1, l+2):
                                if (ll in cubes[ii][jj][kk]
                                    and not (ii == i and jj == j and kk == k and ll == l)
                                    and cubes[ii][jj][kk][ll] == ACTIVE):
                                    result += 1
    
    return result

def get_next_cube(cubes, i, j, k, l):
    cube = cubes[i][j][k][l]
    active_neighbors = get_active_neighbors(cubes, i, j, k, l)
    if ((cube == ACTIVE and (active_neighbors == 2 or active_neighbors == 3))
        or (cube == INACTIVE and active_neighbors == 3)):
        return ACTIVE
    
    return INACTIVE

def pad_cubes(cubes):
    min_i = min(cubes.keys())
    cubes[min_i-1] = {}
    max_i = max(cubes.keys())
    cubes[max_i+1] = {}
    for j in cubes[0].keys():
        cubes[min_i-1][j] = {}
        cubes[max_i+1][j] = {}
        for k in cubes[0][j].keys():
            cubes[min_i-1][j][k] = {}
            cubes[max_i+1][j][k] = {}
            for l in cubes[0][j][k].keys():
                cubes[min_i-1][j][k][l] = INACTIVE
                cubes[max_i+1][j][k][l] = INACTIVE

    for i in cubes.keys():
        min_j = min(cubes[i].keys())
        cubes[i][min_j-1] = {}
        max_j = max(cubes[i].keys())
        cubes[i][max_j+1] = {}
        for k in cubes[i][0].keys():
            cubes[i][min_j-1][k] = {}
            cubes[i][max_j+1][k] = {}
            for l in cubes[i][0][k].keys():
                cubes[i][min_j-1][k][l] = INACTIVE
                cubes[i][max_j+1][k][l] = INACTIVE
    
    for i in cubes.keys():
        for j in cubes[i].keys():
            min_k = min(cubes[i][j].keys())
            max_k = max(cubes[i][j].keys())
            cubes[i][j][min_k-1] = {}
            cubes[i][j][max_k+1] = {}
            for l in cubes[i][j][0].keys():
                cubes[i][j][min_k-1][l] = INACTIVE
                cubes[i][j][max_k+1][l] = INACTIVE
    
    for i in cubes.keys():
        for j in cubes[i].keys():
            for k in cubes[i][j].keys():
                min_l = min(cubes[i][j][k].keys())
                cubes[i][j][k][min_l-1] = INACTIVE
                max_l = max(cubes[i][j][k].keys())
                cubes[i][j][k][max_l+1] = INACTIVE

def get_active_cubes_after_simulation(cubes):
    for cycle in range(CYCLES):
        next_cubes = copy.deepcopy(cubes)
        for i in cubes.keys():
            for j in cubes[i].keys():
                for k in cubes[i][j].keys():
                    for l in cubes[i][j][k].keys():
                        next_cubes[i][j][k][l] = get_next_cube(cubes, i, j, k, l)
        pad_cubes(next_cubes)
        cubes = next_cubes

    result = 0
    for i in cubes.keys():
        for j in cubes[i].keys():
            for k in cubes[i][j].keys():
                for l in cubes[i][j][k].keys():
                    if cubes[i][j][k][l] == ACTIVE:
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
        cubes[i][j][0] = {}
        cubes[i][j][0][0] = cube

pad_cubes(cubes)

active_cubes = get_active_cubes_after_simulation(cubes)

print("The number of active cubes after the simulation is: " + str(active_cubes))
