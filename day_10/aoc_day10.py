with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

# print(lines)

add = []

for l in lines:
    if l[0] == 'a':
        add.append(0)
        add.append(int(l[5:]))
    else:
        add.append(0)

# print(add)

cycle = 0
signal = 1
signal_history = []

for a in add:
    signal += a
    signal_history.append(signal)

index = [20, 60, 100, 140, 180, 220]
signal_sum = 0

for i in index:
    signal_sum += i * signal_history[i-2]
    # print(signal_history[i-1])

print(signal_sum)



