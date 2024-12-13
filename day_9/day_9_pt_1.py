diskmap = ''

with open('day_9\input.txt', 'r') as file:
    for line in file.readlines():
        diskmap += line

blocks = []
current_id = 0
is_file = True
for i in range(len(diskmap)):
    remaining_block_size = int(diskmap[i])
    if is_file:
        while remaining_block_size > 0:
            blocks.append(current_id)
            remaining_block_size -= 1
        current_id += 1
        is_file = False
    else:
        while remaining_block_size > 0:
            blocks.append('.')
            remaining_block_size -= 1
        is_file = True

for i in range(len(blocks)-1, -1, -1):
    if blocks[i] != '.':
        next_free_id = blocks.index('.')
        if next_free_id > i:
            break
        else:
            blocks[next_free_id],blocks[i] = blocks[i],blocks[next_free_id]

checksum = 0
for i in range(len(blocks)):
    if blocks[i] == '.':
        break
    else:
        checksum += i * blocks[i]

print(checksum)