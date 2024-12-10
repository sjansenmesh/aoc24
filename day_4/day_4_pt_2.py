# get input and convert to matrix
rows = []

with open('day_4\input.txt', 'r') as file:
    for line in file.readlines():
        rows.append(line.replace('\n', ''))

# convert input to matrix of characters
matrix = []

for i in range(len(rows)):
    res = []
    res[:] = rows[i]
    matrix.append(res)

# define function to get diagonals of a given point in the matrix
def get_diagonals(matrix, i, j):
    back_slash = ""
    forward_slash = ""
    if i+1 < len(matrix) and j+1 < len(matrix[0]) and i-1 >= 0 and j-1 >= 0:
        back_slash = matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1]
        forward_slash = matrix[i+1][j-1] + matrix[i][j] + matrix[i-1][j+1]
    return (back_slash, forward_slash)

# Scan through matrix for the letter A, get three-letter strings on each diagonal,
# and check for two instances of 'MAS' or 'SAM
count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'A':
            (back_slash, forward_slash) = get_diagonals(matrix, i, j)
            if back_slash in ['MAS', 'SAM'] and forward_slash in ['MAS', 'SAM']:
                count += 1
            
print(count)
