with open('aoc_input5.1.txt') as file:
    lines = [line.replace('\n', '') if line != '\n' else line for line in file]

index = 0

for i in lines:
    if i != '\n':
        index += 1
    else:
        break

crates = lines[:index]
remove_string = lines[index - 1]
move = lines[index + 1:]

lines.remove(remove_string)

max_idx = len(remove_string)

max_station = max([int(new_string) for new_string in str.split(remove_string) if new_string.isdigit()])

# print(crates)
# print(move)

reverse_station = []

for i in range(max_station):
    reverse_station.append([])

for i in crates:
    for x in range(max_idx):
        if i[x].isalpha():
            # print(i[x])
            # print(i.index(i[x]) // 4)
            reverse_station[x // 4].append(i[x])

station = []
for s in reverse_station:
    station.append(s[::-1])

# print(station)

move_list = []
for m in move:
    numbers = [int(new_string) for new_string in str.split(m) if new_string.isdigit()]
    move_list.append(numbers)

# print(move_list)

# [1,2,1] move 1 from 2 to 1
# move 3 from 1 to 2

for m in move_list:
    # print(m)
    no_of_element = m[0]
    from_where = m[1]-1
    to_where = m[2]-1

    # Part 1 movement

    for i in range(no_of_element):
        station[to_where].append(station[from_where][-1])
        station[from_where] = station[from_where][:-1]

    # Part 2 movement

    # holding_crate = []
    # for i in range(no_of_element):
    #     holding_crate.append(station[from_where][-1])
    #     station[from_where] = station[from_where][:-1]
    #
    # holding_crate_reverse = holding_crate[::-1]
    #
    # for h in holding_crate_reverse:
    #     station[to_where].append(h)

    # print(station)

final_station = station[0][-1]

for i in range(1, len(station)):
    final_station += station[i][-1]

print(final_station)