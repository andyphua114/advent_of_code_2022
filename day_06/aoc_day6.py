from collections import Counter

with open('aoc_input6.1.txt') as file:
    lines = [line.rstrip() for line in file]

signal = lines[0]

print(signal)

start_index = 0
found = True
while found:
    marker = signal[start_index:start_index+4]
    detect = (Counter(marker))
    if detect[max(detect, key=detect.get)] > 1:
        start_index += marker.find(max(detect, key=detect.get)) + 1
        detect.clear()
    else:
        start_index += 4
        found = False

print(start_index)

end_index = 0
found = True
while found:
    marker = signal[end_index:end_index+14]
    detect = (Counter(marker))
    if detect[max(detect, key=detect.get)] > 1:
        end_index += marker.find(max(detect, key=detect.get)) + 1
        detect.clear()
    else:
        end_index += 14
        found = False

print(end_index)
