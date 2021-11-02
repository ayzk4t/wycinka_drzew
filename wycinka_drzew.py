import itertools

def isColision(comb, min_s):
    if len(comb) == 1:
        return False
    for x in range(len(comb)):
        if x == 0:
            if (abs(comb[x + 1] - comb[x])) < min_s:
               return True
        elif x == len(comb) - 1:
            if (abs(comb[x] - comb[x - 1])) < min_s:
                return True
        else:
            if ((comb[x + 1] - comb[x]) < min_s) or \
                    ((comb[x] - comb[x - 1]) < min_s):
                return True
    return False

trees_numbers, min_space = input().split()
trees_numbers = int(trees_numbers)
min_space = int(min_space)

position = input().split()
position = [int(x) for x in position]

height = input().split()
height = [int(h) for h in height]
# trees_numbers = 200_000
# min_space = 100
# position = [x for x in range(2,400_001,2)]
# height = [h for h in range(1,200_001)]

tree_dict = {}
for x in range(len(position)):
    tree_dict[position[x]] = [x+1, height[x]]

suspects = []
cut_trees = []
combinations = []
min_height = sum(height)
left_trees = ()
max_cut_height = 0

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
for suspect in suspects:
    max_cut_height += tree_dict[suspect][1]

for c in range(1,len(suspects)):
    combinations += list(itertools.combinations(suspects, c))

for comb in combinations:
    left_height = 0
    if isColision(comb, min_space) == False:
        for c in comb:
            left_height += tree_dict[c][1]
        cuted_height = max_cut_height - left_height
        if cuted_height < min_height:
            min_height = cuted_height
            left_trees = comb

for tree in left_trees:
    if tree in suspects:
        suspects.remove(tree)
print(f"Minimalna suma wysokości drzew przeznaczonych do wycinki: {min_height}")
print(f"Liczba drzew przeznaczonych do wycinki: {len(suspects)}")
print("Drzewa przeznaczone do wycinki: ", end='')
for tree in suspects:
    print(tree_dict[tree][0], end=' ')

