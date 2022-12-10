import re
from collections import defaultdict

with open('aoc_input7.1.txt') as file:
    section = [line.rstrip() for line in file]

# print(section)

level = 0
indicator = 0
dir_level = {}
current = 'root'
dir_size = defaultdict(list)
bypass_list = []

for s in section:

    # cd / means go back to root folder, so level = 0
    if s == '$ cd /':
        level = 0
        current = 'root'
        indicator = 'change_dir'

    # cd \w+ means changing to that directory, so level += 1
    # use current to store the path -> like root_a, where dir a is one level below root
    if re.match(r"\$ cd \w+", s) and s != '$ cd /':
        level += 1
        indicator = 'change_dir'
        find_current = re.findall(r"\$ cd (\w+)", s)
        current = current + "_" + find_current[0]

    # cd .. means go back one level, so level -= 1
    # change current to reflect going back e.g. root_a -> cd .. - > root
    if s == '$ cd ..':
        level -= 1
        current = current.rsplit("_", 1)[0]
        indicator = 'change_dir'

    # if ls, then we want to start consolidating the file size
    # since it may contain sub dir and files, we need to check which is which
    # dir size is where we store the file sizes for each dir
    # if dir a contains sub dir e, file1 size 10, file2 size 20, it will be root_a: [root_a_e, 10, 20]
    if indicator == 'list':
        if re.match(r"dir (\w+)", s):
            location = re.findall(r"dir (\w+)", s)
            dir_size[current].append(current + "_" + location[0])
            dir_level[current] = level
        elif s[0].isdigit():
            file_size = re.findall(r"(\d+)", s)
            dir_size[current].append(file_size[0])
            dir_level[current] = level

    # if ls, then subsequent command will be the lists of dir and files
    if s == '$ ls':
        if current not in bypass_list:
            bypass_list.append(current)
            indicator = 'list'


# print(dir_size)
# print(bypass_list)

# sort the consolidated list of dir and subdir and their corresponding level
# root will be 0, root_a will be 1, root_a_e will be 2
sorted_dir_level = {k: v for k, v in sorted(dir_level.items(), reverse=True, key=lambda item: item[1])}

# print(sorted_dir_level)


final_dir = dict(dir_size)
holding_dir = {}
ultimate_dir = {}

# start consolidating the file sizes for each sub dir upwards, starting from the deepest/lowest level
# since the sub dir at the deepest/lowest level will only have files, and hence only file sizes in dir_size
# at each iteration, use the consolidated sub dir total size for higher level consolidation
for k in sorted_dir_level.keys():
    total = 0
    index = 0
    for v in final_dir[k]:
        if v.isdigit():
            total += int(v)
            index += 1
        elif v in ultimate_dir:
            total += ultimate_dir[v]
            index += 1
        if index == len(final_dir[k]):
            ultimate_dir[k] = total

# print(dir_level)

total_size = 0

for v in ultimate_dir.values():
    if v <= 100000:
        total_size += v

print(total_size)

sorted_ultimate_dir = {k: v for k, v in sorted(ultimate_dir.items(), key=lambda item: item[1])}

# print(sorted_ultimate_dir)

for k, v in sorted_ultimate_dir.items():
    if v >= 30000000 - (70000000 - sorted_ultimate_dir['root']):
        delete_dir = v
        break

print(delete_dir)


