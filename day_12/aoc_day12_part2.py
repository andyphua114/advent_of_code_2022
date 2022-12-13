with open("input.txt") as file:
    old_lines = [line.rstrip() for line in file]

# print(old_lines)


def find_index(x, search):
    row_index = 0

    for row in x:
        col_index = 0
        for col in row:
            if col == search:
                return row_index, col_index
            col_index += 1
        row_index += 1


def check_grid(cur, ne, stepping_dict, visited_array, unvisited_array, line):
    if ne in stepping_dict.keys():
        if ne not in visited:
            first = line[cur[0]][cur[1]]
            second = line[ne[0]][ne[1]]
            if ord(first) == ord(second) - 1 or ord(first) >= ord(second):
                edge = stepping_dict[cur] + 1
                if edge < stepping_dict[ne]:
                    stepping_dict[ne] = edge
    # return stepping_dict


end_index = find_index(old_lines, "E")

lines = []

for i in old_lines:
    i = i.replace("S", "a")
    i = i.replace("E", "z")
    lines.append(i)

start = []

# print(lines)

row_index = 0
for row in lines:
    col_index = 0
    for col in row:
        if col == "a":
            start.append((row_index, col_index))
        col_index += 1
    row_index += 1

print(len(start))

start_point = {}

max_row = len(lines)
max_col = len(lines[0])


print(max_row)
print(max_col)

count_index = 0

for start_index in start:

    unvisited = [start_index]
    visited = []

    for i in range(max_row):
        for j in range(max_col):
            if (i, j) != start_index:
                unvisited.append((i, j))

    step_dict = {}

    for i in unvisited:
        if i == start_index:
            step_dict[i] = 0
        else:
            step_dict[i] = 9999

    current = start_index

    while len(unvisited) != 0:
        i = current
        new = (i[0]-1, i[1])  # check left
        check_grid(current, new, step_dict, visited, unvisited, lines)
        new = (i[0]+1, i[1])  # check right
        check_grid(current, new, step_dict, visited, unvisited, lines)
        new = (i[0], i[1]+1)  # check bottom
        check_grid(current, new, step_dict, visited, unvisited, lines)
        new = (i[0], i[1]-1)  # check top
        check_grid(current, new, step_dict, visited, unvisited, lines)

        visited.append(i)
        unvisited.remove(i)

        if len(unvisited) != 0 or end_index not in visited:
            current_value = step_dict[unvisited[0]]
            current = unvisited[0]
            for u in unvisited:
                if step_dict[u] < current_value:
                    current_value = step_dict[u]
                    current = u
        else:
            break

    start_point[start_index] = step_dict[end_index]
    count_index += 1
    print(count_index)

# print(start_point)
print(min(start_point.values()))
