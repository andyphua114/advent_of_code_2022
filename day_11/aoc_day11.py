import re
from collections import defaultdict


class Monkey:

    def __init__(self, items, worry, decision, yes, no, inspect):
        self.items = items
        self.worry = worry
        self.decision = decision
        self.yes = yes
        self.no = no
        self.inspect = inspect


def worry_operation(symbol, item, worry):
    if worry.isnumeric():
        worry = int(worry)
        if symbol == '+':
            return item + worry
        elif symbol == '-':
            return item - worry
        elif symbol == '*':
            return item * worry
    else:
        if symbol == '+':
            return item + item
        elif symbol == '-':
            return item - item
        elif symbol == '*':
            return item * item


with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

# print(lines)

monkey_list = []
temp = []

for l in lines:
    if l != '':
        temp.append(l.strip())
    else:
        monkey_list.append(temp)
        temp = []

monkey_list.append(temp)

for m in monkey_list:
    m[0] = int(re.findall(r"\d+", m[0])[0])  # extract monkey number
    temp_m1 = re.findall(r"\d+", m[1])  # items to inspect as a list
    m1 = []
    for t in temp_m1:
        m1.append(int(t))
    m[1] = m1
    op1 = m[2][21]
    op2 = m[2][23:]
    m[2] = []
    m[2].append(op1)
    m[2].append(op2)  # action as a list - [0] is arithmetic, [1] is number or old
    m[3] = re.findall(r"\d+", m[3])  # divisible then decide
    m[4] = re.findall(r"\d+", m[4])  # if yes throw to this number
    m[5] = re.findall(r"\d+", m[5])  # if no throw to this number

print(monkey_list)

monkey_group = defaultdict()

# print(len(monkey_list))

for i in range(len(monkey_list)):
    monkey_group[i] = Monkey(monkey_list[i][1], monkey_list[i][2], monkey_list[i][3], monkey_list[i][4], monkey_list[i][5], 0)

end_round = 20
round  = 1

while round != end_round+1:
    for i in range(len(monkey_list)):
        current_monkey = monkey_group[i]
        item_holding = current_monkey.items.copy()
        for item in item_holding:
            current_monkey.inspect += 1
            new_worry = (worry_operation(current_monkey.worry[0], item, current_monkey.worry[1])) // 3
            yes_no = new_worry % int(current_monkey.decision[0])
            if yes_no == 0:
                current_monkey.items.remove(item)
                monkey_group[int(current_monkey.yes[0])].items.append(new_worry)
            else:
                current_monkey.items.remove(item)
                monkey_group[int(current_monkey.no[0])].items.append(new_worry)
    round += 1

inspect_count = []
for i in range(len(monkey_list)):
    inspect_count.append(monkey_group[i].inspect)

inspect_count.sort(reverse = True)
print(inspect_count[0] * inspect_count[1])






