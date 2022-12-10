with open('aoc_input4.1.txt') as file:
    section = [line.rstrip() for line in file]

# print(section)

is_pair = 0
is_overlap = 0

for s in section:
    a, b = s.split(sep=',')
    a1, a2 = a.split(sep='-')
    b1, b2 = b.split(sep='-')
    A = set(range(int(a1), int(a2)+1))
    B = set(range(int(b1), int(b2)+1))

    # Part 1
    if A.issubset(B) or B.issubset(A):
        is_pair += 1

    # Part 2
    if len(A.intersection(B)) != 0:
        is_overlap += 1

print(is_pair)
print(is_overlap)
