with open('aoc_input2.1.txt') as f:
    contents = f.readlines()

# print(contents)

# Part 1

game = []
for i in contents:
    game.append(i.replace('\n', '').split(' '))

print(game)

# A rock, B paper, C scissors [0]
# X rock, Y paper, Z scissors [1]
# win +6, draw +3, lose +0
# rock +1, paper +2, scissors +3
score = 0

for i in game:

    if i[1] == 'X':
        if i[0] == 'A':
            score += 4
        elif i[0] == 'B':
            score += 1
        else:
            score += 7
    if i[1] == 'Y':
        if i[0] == 'B':
            score += 5
        elif i[0] == 'A':
            score += 8
        else:
            score += 2
    if i[1] == 'Z':
        if i[0] == 'C':
            score += 6
        elif i[0] == 'A':
            score += 3
        else:
            score += 9
print(len(game))
print(score)

# X means lose, Y means draw, Z means win

# Part 2

score_dict = {'rock':1,'paper':2,'scissors':3}

score = 0

for i in game:
    if i[1] == 'X': # lose
        if i[0] == 'A':  # rock
            score += score_dict['scissors']
        elif i[0] == 'B':  # paper
            score += score_dict['rock']
        else:  # scissors
            score += score_dict['paper']
    elif i[1] == 'Y':  # draw
        if i[0] == 'A':  # rock
            score += (score_dict['rock'] + 3)
        elif i[0] == 'B':  # paper
            score += (score_dict['paper'] + 3)
        else:  # scissors
            score += (score_dict['scissors'] + 3)

    else:
        if i[0] == 'A':  # rock
            score += (score_dict['paper'] + 6)
        elif i[0] == 'B':  # paper
            score += (score_dict['scissors'] + 6)
        else:  # scissors
            score += (score_dict['rock'] + 6)

print(score)
