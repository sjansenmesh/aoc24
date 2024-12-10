import re

# get input

content = ''

with open('day_3\input.txt', 'r') as file:
    for line in file.readlines():
        content += line

# find all instances of correct mul function
pattern = 'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
matches = re.findall(pattern, content)

# define function to multiply inputs from string
def multiply_inputs(string):
    pattern = 'mul\((\d{1,3},\d{1,3})\)'
    match = re.findall(pattern, string)
    (el1, el2) = match[0].split(',')
    return int(el1) * int(el2)

# multiply matches and get result
result = 0
enabled = True
for i in range(len(matches)):
    string = matches[i]
    match string:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            if enabled:
                result += multiply_inputs(string)
            else:
                continue

print(result)