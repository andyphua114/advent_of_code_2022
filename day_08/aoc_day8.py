from collections import defaultdict

with open("aoc_input8.1.txt") as file:
    lines = [line.rstrip() for line in file]

grid = []

for l in lines:
    r = []
    for c in l:
        r.append(int(c))
    grid.append(r)

print(grid)

len_col = len(grid[0])
len_row = len(grid)

outer_visible = len_col * 2 + (len_row - 2) * 2


row_dict = {}
temp_col_dict = defaultdict(list)

row_index = 0

for tree_row in grid:
    row_dict[row_index] = tree_row
    row_index += 1

for tree_row in grid:
    col_index = 0
    for tree in tree_row:
        temp_col_dict[col_index].append(tree)
        col_index += 1

col_dict = dict(temp_col_dict)

# Part 1

tree_visible = 0

row_index = 0
col_index = 0

for tree_row in grid:  # by row
    if (row_index != 0) and (row_index != (len_row - 1)):
        col_index = 0
        for tree in tree_row:  # by tree in each row
            if (col_index != 0) and (col_index != (len_col - 1)):

                r1 = max(row_dict[row_index][:col_index])
                r2 = max(row_dict[row_index][col_index+1:])

                c1 = max(col_dict[col_index][:row_index])
                c2 = max(col_dict[col_index][row_index+1:])

                if tree > r1 or tree > r2 or tree > c1 or tree > c2:
                    tree_visible += 1
            col_index += 1
    row_index += 1

print(tree_visible+outer_visible)

# Part 2

scenic_score = 0

row_index = 0
col_index = 0

for tree_row in grid:  # by row
    if (row_index != 0) and (row_index != (len_row - 1)):
        col_index = 0
        for tree in tree_row:  # by tree in each row
            if (col_index != 0) and (col_index != (len_col - 1)):

                r1 = (row_dict[row_index][:col_index])
                r1.reverse()
                r2 = (row_dict[row_index][col_index+1:])

                c1 = (col_dict[col_index][:row_index])
                c1.reverse()
                c2 = (col_dict[col_index][row_index+1:])

                r1_score = 0
                r2_score = 0
                c1_score = 0
                c2_score = 0

                for i in r1:
                    if i < tree:
                        r1_score += 1
                    else:
                        r1_score += 1
                        break
                for i in r2:
                    if i < tree:
                        r2_score += 1
                    else:
                        r2_score += 1
                        break
                for i in c1:
                    if i < tree:
                        c1_score += 1
                    else:
                        c1_score += 1
                        break
                for i in c2:
                    if i < tree:
                        c2_score += 1
                    else:
                        c2_score += 1
                        break

                current_scenic_score = r1_score * r2_score * c1_score * c2_score

                if current_scenic_score > scenic_score:
                    scenic_score = current_scenic_score

            col_index += 1

    row_index += 1

print(scenic_score)