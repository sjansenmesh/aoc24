# get input
rows = []

with open('day_7\input.txt', 'r') as file:
    for line in file.readlines():
        target, numbers = line.split(':')
        number_list = numbers.strip().split(' ')
        number_list = list(map(int, number_list))
        rows.append([int(target), number_list])

def recursive_operate(results, numbers):
    new_results = []
    y = numbers[0]
    numbers = numbers[1:]
    for x in results:
        add = x + y
        new_results.append(add)
        multiply = x * y
        new_results.append(multiply)
    if len(numbers) > 0:
        return recursive_operate(new_results, numbers)
    else:
        return new_results

achieved = []

for row in rows:
    target = row[0]
    start = row[1][0]
    numbers = row[1][1:]
    potentials = recursive_operate([start], numbers)
    if target in potentials:
        achieved.append(target)

print(sum(achieved))