f = open("advent_2022_23_input.txt")
#f = open("test_input.txt")

lines = [line.strip("\n") for line in f.readlines()]

f.close()

elves = []
elves_set = set()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            elves.append((x, y))

global_order = 0
movement = True

def neighbours_count(position):
    for y in range(-1, 2):
        for x in range(-1, 2):
            if y == 0 and x == 0:
                continue
            if (position[0] + x, position[1] + y) in elves_set:
                return 1
    return 0

def get_proposed_step(position):
    global global_order
    for order in range(global_order, global_order + 4):
        order %= 4
        if order == 0 and ((position[0] - 1, position[1] - 1) not in elves_set and (position[0], position[1] - 1) not in elves_set and (position[0] + 1, position[1] - 1) not in elves_set):
            return (position[0], position[1] - 1)
        if order == 1 and ((position[0] - 1, position[1] + 1) not in elves_set and (position[0], position[1] + 1) not in elves_set and (position[0] + 1, position[1] + 1) not in elves_set):
            return (position[0], position[1] + 1)
        if order == 2 and ((position[0] - 1, position[1] - 1) not in elves_set and (position[0] - 1, position[1]) not in elves_set and (position[0] - 1, position[1] + 1) not in elves_set):
            return (position[0] - 1, position[1])
        if order == 3 and ((position[0] + 1, position[1] - 1) not in elves_set and (position[0] + 1, position[1]) not in elves_set and (position[0] + 1, position[1] + 1) not in elves_set):
            return (position[0] + 1, position[1])
    return 0

def move():
    global global_order, movement, elves_set
    steps = {}
    moved = False
    elves_set = set(elves)
    for index, elf in enumerate(elves):
        if neighbours_count(elf) == 0:
            pass
        else:
            step = get_proposed_step(elf)
            if step == 0:
                continue
            if step in steps:
                steps[step].append(index)
            else:
                steps[step] = [index]

    for item in steps:
        if len(steps[item]) == 1:
            moved = True
            elves[steps[item][0]] = item

    global_order += 1
    global_order %= 4

    if not moved:
        movement = False

for _ in range(10):
    move()

max_x, min_x = max([point[0] for point in elves]) + 1, min([point[0] for point in elves])
max_y, min_y = max([point[1] for point in elves]) + 1, min([point[1] for point in elves])

print((max_x - min_x) * (max_y - min_y) - len(elves))