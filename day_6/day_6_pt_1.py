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
        guard_pos = [i, j]
    except:
        continue

# loop over guard movement until it moves out of matrix dimensions
is_in_bounds = True 
guard_direction = 'N'
while is_in_bounds:
    matrix, guard_pos, guard_direction = update_guard_position(matrix, guard_pos, guard_direction)
    is_in_bounds = guard_direction != 'OUT_OF_BOUNDS'

# count Xs in matrix
count = 1
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'X':
            count += 1

print(count)