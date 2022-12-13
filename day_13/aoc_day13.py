import ast


def checker(a, b, index):

    if type(a) == list and len(a) == 0:
        return "right"
    elif type(a) == list and len(a) != 0 and type(b) == list and len(b) == 0:
        return "wrong"
    elif type(a) == list and type(b) == list:
        for j in range(len(a)):
            if j != len(a) and j == len(b):
                return "wrong"
            elif j == len(a)-1 and j < len(b):
                return "right"
            else:
                value = checker(a[j], b[j], index)
                if value == "right" or value == "wrong":
                    return value
    elif type(a) == int and type(b) == int:
        if a < b:
            return "right"
        elif a > b:
            return "wrong"
    elif type(a) == list and type(b) == int:
        temp_b = [b]
        value = checker(a, temp_b, index)
        if value == "right" or value == "wrong":
            return value
    elif type(a) == int and type(b) == list:
        temp_a = [a]
        value = checker(temp_a, b, index)
        if value == "right" or value == "wrong":
            return value


with open("sample.txt") as file:
    old_lines = [line.rstrip() for line in file]

lines = []
temp = []

for i in old_lines:
    if i != '':
        i = ast.literal_eval(i)
        temp.append(i)
    else:
        lines.append(temp)
        temp = []

lines.append(temp)

print(lines)

right = []
wrong = []
index = 1

for i in lines:  # i[0] is left; i[1] is right. can be integer, empty list, or list of list
    value = checker(i[0], i[1], index)
    if value == "right":
        right.append(index)
    else:
        wrong.append(index)
    print(index)
    index += 1

print(right)