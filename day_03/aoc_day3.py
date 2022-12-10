import string

with open('aoc_input3.1.txt') as file:
    ruck = [line.rstrip() for line in file]

# Part 1

lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

alphabet = lower_alphabet + upper_alphabet

alphabet_dict = {}
priority = 1
for i in alphabet:
    alphabet_dict[i] = priority
    priority += 1

priority_score = 0

for r in ruck:
    item_len = int(len(r)/2)
    r1 = set(r[0:item_len])
    r2 = set(r[item_len:])
    common_item = r1.intersection(r2)
    (element,) = common_item
    priority_score += alphabet_dict[element]

print(priority_score)

# Part 2

ruck_group = []
idx = 1
total_len = int(len(ruck)/3)
temp_ruck = []
for r in ruck:
    temp_ruck.append(r)
    if idx % 3 == 0:
        ruck_group.append(temp_ruck)
        temp_ruck = []
        idx = 1
    else:
        idx += 1

badge_priority_score = 0

for rg in ruck_group:
    rg1 = set(rg[0])
    rg2 = set(rg[1])
    rg3 = set(rg[2])
    badge = rg1.intersection(rg2)
    common_badge = badge.intersection(rg3)
    # print(common_badge)
    (element,) = common_badge
    badge_priority_score += alphabet_dict[element]

print(badge_priority_score)
