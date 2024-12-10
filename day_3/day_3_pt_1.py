import re

# get input

content = ''

with open('day_3\input.txt', 'r') as file:
    for line in file.readlines():
        content += line

# find all instances of correct mul function
pattern = 'mul\((\d{1,3},\d{1,3})\)'
matches = re.findall(pattern, content)

# define function to multiply inputs from string
def multiply_inputs(string):
    (el1, el2) = string.split(',')
    return int(el1) * int(el2)

# multiply matches and get result
mults = list(map(multiply_inputs, matches))

print(sum(mults))