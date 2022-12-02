f = open("advent_2022_02_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

total = 0

d = {'X': 0, 'Y': 3, 'Z': 6}

for line in lines:
    p1, p2 = line.split(" ")
    score = d[p2]
    if p1 == 'A':
        if p2 == 'X':
            score += 3
        elif p2 == 'Y':
            score += 1
        else:
            score += 2
    elif p1 == 'B':
        if p2 == 'X':
            score += 1
        elif p2 == 'Y':
            score += 2
        else:
            score += 3
    if p1 == 'C':
        if p2 == 'X':
            score += 2
        elif p2 == 'Y':
            score += 3
        else:
            score += 1
    total += score

print(total)