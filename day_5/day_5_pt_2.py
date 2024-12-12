# Get inout and split into rules and updates
rules = []
updates = []

def split_and_cast(str, delimiter):
    split = str.split(delimiter)
    result = list(map(int, split))
    return result

# Scan though update and get rules that need to be checked
def get_rules_to_check(update):
    rules_to_check = []
    for i in range(len(update)):
        for j in range(len(update)):
            if i == j:
                continue
            elif i < j:
                rules_to_check.append([update[j], update[i]])
            elif i > j:
                rules_to_check.append([update[i], update[j]])
    return rules_to_check

# Check rules against rule list for violations
def check_rules(rules_to_check):
    broken_rules = []
    for rule in rules_to_check:
        if rule in rules:
            if rule not in broken_rules:
                broken_rules.append(rule)
    return broken_rules

# Get input data
with open('day_5\input.txt', 'r') as file:
    for row in file.readlines():
        clean = row.strip('\n')
        if '|' in clean:
            rules.append(split_and_cast(clean, '|'))
        elif ',' in clean:
            updates.append(split_and_cast(clean, ','))

# Identify incorrect updates
incorrect_updates = []

for update in updates:
    rules_to_check = get_rules_to_check(update)
    broken_rules = check_rules(rules_to_check)
    if len(broken_rules) != 0:
        incorrect_updates.append([update, broken_rules])

# Resolve violations by swapping offending elements
def resolve_issues(update, broken_rules):
    for rule in broken_rules:
        i = update.index(rule[0])
        j = update.index(rule[1])
        update[i], update[j] = update[j], update[i]
    return update

# Loop through incorrect updates and keep resolving until no violations remain
resolved_updates = []
for update in incorrect_updates:
    resolved = False
    while not resolved:
        edited_update = resolve_issues(update[0], update[1])
        new_rules_to_check = get_rules_to_check(edited_update)
        new_broken_rules = check_rules(new_rules_to_check)
        update = [edited_update, new_broken_rules]
        if len(new_broken_rules) == 0:
            resolved = True
    resolved_updates.append(update[0])

# Get and sum middle number from each correct update:
sum = 0

for update in resolved_updates:
    middle_page = len(update)//2
    sum += update[middle_page]

print(sum)