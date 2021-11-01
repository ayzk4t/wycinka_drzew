import itertools

trees_numbers, min_space = input().split()
trees_numbers = int(trees_numbers)
min_space = int(min_space)

position = input().split()
position = [int(x) for x in position]

height = input().split()
height = [int(h) for h in height]

suspects = []
cut_trees = []
good = False
min_height = max(height)

for x in range(trees_numbers):
    if x == 0:
        if (position[x+1] - position[x]) < min_space:
            suspects.append(position[x])
    elif x == trees_numbers-1:
        if (position[x] - position[x-1]) < min_space:
            suspects.append(position[x])
    else:
        if ((position[x+1] - position[x]) < min_space) or \
                ((position[x] - position[x-1]) < min_space):
            suspects.append(position[x])

for c in range(1,len(suspects)):
    combinations = list(itertools.combinations(suspects, c))
    temp_list = suspects[:]
    for comb in combinations:
        for tree in comb:
            temp_list.remove(tree)