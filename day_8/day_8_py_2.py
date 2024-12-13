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

grid_height = len(grid)
grid_width = len(grid[0])

# Get all possible antinodes for a given pair of antennas
def get_all_antinodes(coords_1, coords_2, grid_height, grid_width):
    distance = [coords_2[0]-coords_1[0], coords_2[1]-coords_1[1]]
    antinodes = []
    upper_bound_hit = False
    lower_bound_hit = False
    upper_bound_count = 0
    lower_bound_count = 0
    while not upper_bound_hit:
        new_antinode = [coords_2[0]+(distance[0]*upper_bound_count), coords_2[1]+(distance[1]*upper_bound_count)]
        if new_antinode[0] in range(0, grid_height) and new_antinode[1] in range(0, grid_width):
            antinodes.append(new_antinode)
            upper_bound_count += 1
        else:
            upper_bound_hit = True
    while not lower_bound_hit:
        new_antinode = [coords_1[0]-(distance[0]*lower_bound_count), coords_1[1]-(distance[1]*lower_bound_count)]
        if new_antinode[0] in range(0, grid_height) and new_antinode[1] in range(0, grid_width):
            antinodes.append(new_antinode)
            lower_bound_count += 1
        else:
            lower_bound_hit = True
    return antinodes


# Gather unique antinodes across grid
antinodes = []
for frequency in antennas:
    antenna_list = antennas[frequency]
    for i in range(len(antenna_list)):
        for j in range(len(antenna_list)):
            if i < j:
                new_antinodes = get_all_antinodes(antenna_list[i], antenna_list[j], grid_height, grid_width)
                for antinode in new_antinodes:
                    if antinode not in antinodes:
                        antinodes.append(antinode)

print(len(antinodes))