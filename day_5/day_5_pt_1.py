# Get inout and split into rules and updates
rules = []
updates = []

def split_and_cast(str, delimiter):
    split = str.split(delimiter)
    result = list(map(int, split))
    return result

with open('day_5\input.txt', 'r') as file:
    for row in file.readlines():
        clean = row.strip('\n')
        if '|' in clean:
            rules.append(split_and_cast(clean, '|'))
        elif ',' in clean:
            updates.append(split_and_cast(clean, ','))

# Identify correct updates
correct_updates = []

for update in updates:
    rules_to_check = []
    for i in range(len(update)):
        for j in range(len(update)):
            if i == j:
                continue
            elif i < j:
                rules_to_check.append([update[j], update[i]])
            elif i > j:
                rules_to_check.append([update[i], update[j]])
    correct = True
    for rule in rules_to_check:
        if rule in rules:
            correct = False
            break
    if correct:
        correct_updates.append(update)

# Get and sum middle number from each correct update:
sum = 0

for update in correct_updates:
    middle_page = len(update)//2
    sum += update[middle_page]

print(sum)