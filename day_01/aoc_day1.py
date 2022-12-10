with open('input.txt') as f:
    contents = f.readlines()

food = []
total_cal = 0
idx = 0
for i in contents:
    cal = i.replace('\n', '')
    if cal != '':
        total_cal = total_cal + int(cal)
    else:
        food.append(total_cal)
        total_cal = 0
    if idx == len(contents)-1:
        food.append(total_cal)
    idx += 1

print(max(food))

food.sort(reverse=True)

top3_food = 0
for i in range(3):
    top3_food += food[i]

print(top3_food)