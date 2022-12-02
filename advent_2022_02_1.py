f = open("advent_2022_02_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

total = 0

d = {'X': 1, 'Y': 2, 'Z': 3}

for line in lines:
    p1, p2 = line.split(" ")
    score = d[p2]
    if (p1 == 'A' and p2 == 'Y') or (p1 == 'B' and p2 == 'Z') or (p1 == 'C' and p2 == 'X'):
        score += 6
    elif (p1 == 'A' and p2 == 'X') or (p1 == 'B' and p2 == 'Y') or (p1 == 'C' and p2 == 'Z'):
        score += 3
    else:
        score += 0
    total += score

print(total)