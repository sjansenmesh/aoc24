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

# define functions to get four letters in each cardinal direction from a given point in the matrix
def get_east(matrix, i, j):
    if j+3 < len(matrix[0]):
        result = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]
        return result

def get_southeast(matrix, i, j):
    if i+3 < len(matrix) and j+3 < len(matrix[0]):
        result = matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3]
        return result

def get_south(matrix, i, j):
    if i+3 < len(matrix):
        result = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
        return result

def get_southwest(matrix, i, j):
    if i+3 < len(matrix) and j-3 >= 0:
        result = matrix[i][j] + matrix[i+1][j-1] + matrix[i+2][j-2] + matrix[i+3][j-3]
        return result

def get_west(matrix, i, j):
    if j-3 >= 0:
        result = matrix[i][j] + matrix[i][j-1] + matrix[i][j-2] + matrix[i][j-3]
        return result

def get_northwest(matrix, i, j):
    if i-3 >= 0 and j-3 >= 0:
        result = matrix[i][j] + matrix[i-1][j-1] + matrix[i-2][j-2] + matrix[i-3][j-3]
        return result

def get_north(matrix, i, j):
    if i-3 >= 0:
        result = matrix[i][j] + matrix[i-1][j] + matrix[i-2][j] + matrix[i-3][j]
        return result

def get_northeast(matrix, i, j):
    if i-3 >= 0 and j+3 < len(matrix[0]):
        result = matrix[i][j] + matrix[i-1][j+1] + matrix[i-2][j+2] + matrix[i-3][j+3]
        return result

# Scan through matrix for the letter X, get four-letter strings in each cardinal direction,
# and count instances of 'XMAS'
count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'X':
            words = []
            words.append(get_east(matrix, i, j))
            words.append(get_southeast(matrix, i, j))
            words.append(get_south(matrix, i, j))
            words.append(get_southwest(matrix, i, j))
            words.append(get_west(matrix, i, j))
            words.append(get_northwest(matrix, i, j))
            words.append(get_north(matrix, i, j))
            words.append(get_northeast(matrix, i, j))
            count += words.count('XMAS')
            
print(count)
