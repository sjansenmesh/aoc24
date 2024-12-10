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

similarity_score = 0

# loop through elements of list1
for i in range(len(list1)):
    el = list1[i]
    similarity = el * list2.count(el)
    similarity_score += similarity

print(similarity_score)