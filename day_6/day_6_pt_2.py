import copy

def update_guard_direction(current):
    match current:
        case 'N':
            return 'E'
        case 'E':
            return 'S'
        case 'S':
            return 'W'
        case 'W':
            return 'N'
        
def update_guard_position(matrix, guard_pos, guard_direction):
    try:
        match guard_direction:
            case 'N':
                if guard_pos[0] == 0:
                    return matrix, 'OUT_OF_BOUNDS', 'OUT_OF_BOUNDS'
                elif matrix[guard_pos[0]-1][guard_pos[1]] == '#':
                    guard_direction = update_guard_direction(guard_direction)
                    return matrix, guard_pos, guard_direction
                else:
                    matrix[guard_pos[0]][guard_pos[1]] = 'X'
                    return matrix, [guard_pos[0]-1, guard_pos[1]], guard_direction
            case 'E':
                if guard_pos[1] == 0:
                    return matrix, 'OUT_OF_BOUNDS', 'OUT_OF_BOUNDS'
                elif matrix[guard_pos[0]][guard_pos[1]+1] == '#':
                    guard_direction = update_guard_direction(guard_direction)
                    return matrix, guard_pos, guard_direction
                else:
                    matrix[guard_pos[0]][guard_pos[1]] = 'X'
                    return matrix, [guard_pos[0], guard_pos[1]+1], guard_direction
            case 'S':
                if matrix[guard_pos[0]+1][guard_pos[1]] == '#':
                    guard_direction = update_guard_direction(guard_direction)
                    return matrix, guard_pos, guard_direction
                else:
                    matrix[guard_pos[0]][guard_pos[1]] = 'X'
                    return matrix, [guard_pos[0]+1, guard_pos[1]], guard_direction
            case 'W':
                if matrix[guard_pos[0]][guard_pos[1]-1] == '#':
                    guard_direction = update_guard_direction(guard_direction)
                    return matrix, guard_pos, guard_direction
                else:
                    matrix[guard_pos[0]][guard_pos[1]] = 'X'
                    return matrix, [guard_pos[0], guard_pos[1]-1], guard_direction
    except:
        return matrix, 'OUT_OF_BOUNDS', 'OUT_OF_BOUNDS'



# Get input
rows = []

with open('day_6\input.txt', 'r') as file:
    for line in file.readlines():
        rows.append(line.replace('\n', ''))

# convert input to matrix of characters
matrix = []

for i in range(len(rows)):
    res = []
    res[:] = rows[i]
    matrix.append(res)

# find guard's starting position
for i in range(len(matrix)):
    try:
        j = matrix[i].index('^')
        init_guard_pos = [i, j]
    except:
        continue

# get guard's path
is_in_bounds = True 
guard_direction = 'N'
path = [init_guard_pos]
guard_pos = init_guard_pos
while is_in_bounds:
    matrix, guard_pos, guard_direction = update_guard_position(matrix, guard_pos, guard_direction)
    if guard_pos not in path and guard_pos != 'OUT_OF_BOUNDS':
        path.append(guard_pos)
    is_in_bounds = guard_direction != 'OUT_OF_BOUNDS'

count_loops = 0
for position in path:
    matrix_copy = copy.deepcopy(matrix)      
    matrix_copy[position[0]][position[1]] = '#'
    is_in_bounds = True
    not_in_loop = True
    guard_pos = init_guard_pos
    guard_direction = 'N'
    previous_pos = {guard_direction: [guard_pos]}
    while is_in_bounds and not_in_loop:
        matrix_copy, guard_pos, guard_direction = update_guard_position(matrix_copy, guard_pos, guard_direction)
        if guard_direction in previous_pos:
            if guard_pos in previous_pos[guard_direction]:
                not_in_loop = False
                count_loops += 1
            else:
                previous_pos[guard_direction].append(guard_pos)
        else:
                previous_pos[guard_direction] = [guard_pos]
        is_in_bounds = guard_direction != 'OUT_OF_BOUNDS'

print(count_loops)