f = open("advent_2022_14_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

from collections import defaultdict

d = defaultdict(lambda: '.')

depth = 0

def populate_path(paths):
    global depth
    for i in range(1, len(paths)):
        prev = paths[i - 1].split(",")
        current = paths[i].split(",")
        if prev[0] != current[0]:
            for rock in range(min(int(prev[0]), int(current[0])), max(int(prev[0]), int(current[0])) + 1):
                d[(rock, int(current[1]))] = '#'
        elif prev[1] != current[1]:
            for rock in range(min(int(prev[1]), int(current[1])), max(int(prev[1]), int(current[1])) + 1):
                d[(int(current[0]), rock)] = '#'
                depth = max(depth, rock)
        

for line in lines:
    populate_path(line.split(" -> "))

sand_unit = 0

while True:
    pos = (500, 0)
    finished = False
    while not finished:
        if d[(pos[0], pos[1] + 1)] == '.':
            pos = (pos[0], pos[1] + 1)
        elif d[(pos[0] - 1, pos[1] + 1)] == '.':
            pos = (pos[0] - 1, pos[1] + 1)
        elif d[(pos[0] + 1, pos[1] + 1)] == '.':
            pos = (pos[0] + 1, pos[1] + 1)
        else:
            finished = True
            break

        if pos[1] > depth:
            print(sand_unit)
            exit(0)

    d[(pos[0], pos[1])] = 'o'
    sand_unit += 1
