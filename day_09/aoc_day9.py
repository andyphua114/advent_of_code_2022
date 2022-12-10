from math import sqrt

with open("aoc_input9.1.txt") as file:
    lines = [line.rstrip() for line in file]

# print(lines)

path = []

for l in lines:
    repeat = int(l[2:])
    for r in range(repeat):
        path.append(l[0])

# print(path)

path_dict = {'R': 1, 'L': -1, 'U': 1, 'D': -1}
head_current_loc = [0, 0]
tail_current_loc = [0, 0]

head_crumbs = []
tail_crumbs = []

for step in path:
    if step == 'R' or step == 'L':
        head_current_loc[0] += path_dict[step]

    elif step == 'U' or step == 'D':
        head_current_loc[1] += path_dict[step]

    head_history_loc = tuple(head_current_loc)
    head_crumbs.append(head_history_loc)

    distance = sqrt(
        pow((head_current_loc[0] - tail_current_loc[0]), 2) + pow((head_current_loc[1] - tail_current_loc[1]), 2))

    if distance > sqrt(2):
        if head_current_loc[0] == tail_current_loc[0]:
            if head_current_loc[1] > tail_current_loc[1]:
                tail_current_loc[1] += 1
            else:
                tail_current_loc[1] -= 1
        elif head_current_loc[1] == tail_current_loc[1]:
            if head_current_loc[0] > tail_current_loc[0]:
                tail_current_loc[0] += 1
            else:
                tail_current_loc[0] -= 1
        else:
            if sqrt(pow((head_current_loc[0] - (tail_current_loc[0] - 1)), 2) + pow(
                    (head_current_loc[1] - (tail_current_loc[1] + 1)), 2)) <= sqrt(2):
                tail_current_loc[0] -= 1
                tail_current_loc[1] += 1
            elif sqrt(pow((head_current_loc[0] - (tail_current_loc[0] - 1)), 2) + pow(
                    (head_current_loc[1] - (tail_current_loc[1] - 1)), 2)) <= sqrt(2):
                tail_current_loc[0] -= 1
                tail_current_loc[1] -= 1
            elif sqrt(pow((head_current_loc[0] - (tail_current_loc[0] + 1)), 2) + pow(
                    (head_current_loc[1] - (tail_current_loc[1] + 1)), 2)) <= sqrt(2):
                tail_current_loc[0] += 1
                tail_current_loc[1] += 1
            elif sqrt(pow((head_current_loc[0] - (tail_current_loc[0] + 1)), 2) + pow(
                    (head_current_loc[1] - (tail_current_loc[1] - 1)), 2)) <= sqrt(2):
                tail_current_loc[0] += 1
                tail_current_loc[1] -= 1

    tail_history_loc = tuple(tail_current_loc)
    tail_crumbs.append(tail_history_loc)

# print(head_current_loc)
# print(tail_current_loc)
# print(head_crumbs)
# print(tail_crumbs)

print(len(set(tail_crumbs)))


# Part 2


def check_path(first, second, pathway, index):
    path_dict = {'R': 1, 'L': -1, 'U': 1, 'D': -1}
    if index == 0:
        if pathway == 'R' or pathway == 'L':
            first[0] += path_dict[pathway]

        elif pathway == 'U' or pathway == 'D':
            first[1] += path_dict[pathway]

    dist = sqrt(pow((first[0] - second[0]), 2) + pow((first[1] - second[1]), 2))

    if dist > sqrt(2):
        if first[0] == second[0]:
            if first[1] > second[1]:
                second[1] += 1
            else:
                second[1] -= 1
        elif first[1] == second[1]:
            if first[0] > second[0]:
                second[0] += 1
            else:
                second[0] -= 1
        else:
            if sqrt(pow((first[0] - (second[0] - 1)), 2) + pow((first[1] - (second[1] + 1)), 2)) <= sqrt(2):
                second[0] -= 1
                second[1] += 1
            elif sqrt(pow((first[0] - (second[0] - 1)), 2) + pow((first[1] - (second[1] - 1)), 2)) <= sqrt(2):
                second[0] -= 1
                second[1] -= 1
            elif sqrt(pow((first[0] - (second[0] + 1)), 2) + pow((first[1] - (second[1] + 1)), 2)) <= sqrt(2):
                second[0] += 1
                second[1] += 1
            elif sqrt(pow((first[0] - (second[0] + 1)), 2) + pow((first[1] - (second[1] - 1)), 2)) <= sqrt(2):
                second[0] += 1
                second[1] -= 1

    if index == 8:
        nine_history_loc = tuple(second)
        return nine_history_loc


with open("aoc_input9.1.txt") as file:
    lines = [line.rstrip() for line in file]

# print(lines)

path = []

for l in lines:
    repeat = int(l[2:])
    for r in range(repeat):
        path.append(l[0])

rope = []
for i in range(10):
    rope.append([0, 0])

final = []

for p in path:
    for i in range(len(rope)-1):
        final.append(check_path(rope[i], rope[i+1], p, i))

res = list(filter(lambda item: item is not None, final))
t = set(res)

print(len(t))

