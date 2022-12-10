with open("sample.txt") as file:
    lines = [line.rstrip() for line in file]

# print(lines)

instructions = []
add = []

for l in lines:
    if l[0] == 'a':
        add.append(int(l[5:]))
    else:
        add.append(0)
    instructions.append(l[0])

# print(add)

cycle = 0
signal = 1
signal_history = []

for i in instructions:
    if i == 'n':
        signal_history.append(signal)
        cycle += 1
    else:
        signal_history.append(signal)
        signal += add[cycle]
        signal_history.append(signal)
        cycle += 1

index = [20, 60, 100, 140, 180, 220]
signal_sum = 0

for i in index:
    signal_sum += i * signal_history[i-1]
    # print(signal_history[i-1])

# print(signal_sum)
print(signal_history)



