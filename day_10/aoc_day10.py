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

# Part 1

signal = 1
signal_history = []

for a in add:
    signal += a
    signal_history.append(signal)

index = [20, 60, 100, 140, 180, 220]
signal_sum = 0

for i in index:
    signal_sum += i * signal_history[i-2]

print(signal_sum)

# Part 2


def prt_output(signal):
    pattern = ["."] * 40
    index = 0
    prev = 0
    for s in signal:
        # we use prev value to check and print because the register only moves at the end of the second cycle of addx
        if index == prev-1 or index == prev or index == prev+1:
            pattern[index] = "#"
        prev = s
        index += 1

    print(''.join(pattern))


prt_output(signal_history[:40])
prt_output(signal_history[40:80])
prt_output(signal_history[80:120])
prt_output(signal_history[120:160])
prt_output(signal_history[160:200])
prt_output(signal_history[200:240])


