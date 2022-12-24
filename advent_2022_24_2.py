f = open("advent_2022_24_input.txt")
#f = open("test_input.txt")

lines = [line.strip("\n") for line in f.readlines()]

f.close()

GRID_WIDTH = len(lines[0])
GRID_HEIGHT = len(lines)
DIRS = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}

blizzards = {}
blizzard_dict = {}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '^':
            direction = 'U'
        elif char == '>':
            direction = 'R'
        elif char == 'v':
            direction = 'D'
        elif char == '<':
            direction = 'L'
        else:
            continue

        if (x, y) not in blizzard_dict:
            blizzard_dict[(x, y)] = [direction]
        else:
            blizzard_dict[(x, y)].append(direction)

blizzards[0] = blizzard_dict

def construct_blizzard(minute):
    global blizzards
    blizzard_dict = {}

    for position in blizzards[minute - 1]:
        for dir in blizzards[minute - 1][position]:
            new_pos = (position[0] + DIRS[dir][0], position[1] + DIRS[dir][1])

            if dir == 'U' and new_pos[1] == 0:
                new_pos = (new_pos[0], GRID_HEIGHT - 2)
            elif dir == 'R' and new_pos[0] == GRID_WIDTH - 1:
                new_pos = (1, new_pos[1])
            elif dir == 'D' and new_pos[1] == GRID_HEIGHT - 1:
                new_pos = (new_pos[0], 1)
            elif dir == 'L' and new_pos[0] == 0:
                new_pos = (GRID_WIDTH - 2, new_pos[1])
            
            if new_pos not in blizzard_dict:
                blizzard_dict[new_pos] = [dir]
            else:
                blizzard_dict[new_pos].append(dir)

    blizzards[minute] = blizzard_dict

start_pos = (1, 0)
end_pos = (GRID_WIDTH - 2, GRID_HEIGHT - 1)

frontier = [(start_pos, 0)]
destination = 0
times = []

seen = set()

while frontier:
    found = False
    position, minute = frontier.pop(0)

    if minute not in blizzards:
        construct_blizzard(minute)

    if position in blizzards[minute]:
        continue

    if (minute, position[0], position[1]) in seen:
        continue
    else:
        seen.add((minute, position[0], position[1]))

    for dir in DIRS:
        new_pos = (position[0] + DIRS[dir][0], position[1] + DIRS[dir][1])
        if new_pos == end_pos:
            if destination == 0:
                times.append(minute + 1)
                destination = 1
                found = True
                frontier = [(new_pos, minute + 1)]
                end_pos = (1, 0)
                seen = set()
                break
            if destination == 1:
                times.append(minute + 1)
                destination = 2
                found = True
                frontier = [(new_pos, minute + 1)]
                end_pos = (GRID_WIDTH - 2, GRID_HEIGHT - 1)
                seen = set()
                break
            if destination == 2:
                times.append(minute + 1)
                print(times)
                exit(0)
        if new_pos[0] == 0 or new_pos[0] == GRID_WIDTH - 1 or new_pos[1] <= 0 or new_pos[1] >= GRID_HEIGHT - 1:
            continue
        frontier.append((new_pos, minute + 1))

    if not found:
        frontier.append((position, minute + 1))