grid = []

with open('day_8\input.txt', 'r') as file:
    for row in file.readlines():
        grid.append(row.strip())

# identify antennas
antennas = {}

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.':
            if grid[i][j] in antennas:
                antennas[grid[i][j]].append([i, j])
            else:
                antennas[grid[i][j]] = [[i,j]]

# identify possible antinodes
possible_antinodes = []
for frequency in antennas:
    antenna_list = antennas[frequency]
    for i in range(len(antenna_list)):
        for j in range(len(antenna_list)):
            if i < j:
                distance = [antenna_list[j][0]-antenna_list[i][0], antenna_list[j][1]-antenna_list[i][1]]
                possible_antinodes.append([antenna_list[i][0]-distance[0], antenna_list[i][1]-distance[1]])
                possible_antinodes.append([antenna_list[j][0]+distance[0], antenna_list[j][1]+distance[1]])

# filter out antinodes outside grid
grid_height = len(grid)
grid_width = len(grid[0])
antinodes = [coord for coord in possible_antinodes if coord[0] >= 0 and coord[0] < grid_height and coord[1] >= 0 and coord[1] < grid_width]

# get unique antinodes
unique_antinodes = []
for antinode in antinodes:
    if antinode not in unique_antinodes:
        unique_antinodes.append(antinode)
print(len(unique_antinodes))