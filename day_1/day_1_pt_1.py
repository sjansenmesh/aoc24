# get input
f = open('day_1\input.txt', 'r')

# split input into two lists
list1 = []
list2 = []

for row in f.readlines():
    (el1, el2) = row.split('   ')
    list1.append(int(el1))
    list2.append(int(el2))

# sort lists
list1.sort()
list2.sort()

# find difference between each pair
diffs = []
for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    diffs.append(diff)

# sum up differences
print(sum(diffs))