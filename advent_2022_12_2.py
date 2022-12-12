f = open("advent_2022_12_input.txt")
#f = open("test_input.txt")

lines = [[tree for tree in line.strip()] for line in f.readlines()]

f.close()

GRID_HEIGHT = len(lines)
GRID_WIDTH = len(lines[0])

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

frontier = []

for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        if lines[y][x] == 'S' or lines[y][x] == 'a':
            frontier.append((x, y, 0))
            lines[y][x] = 'a'
        elif lines[y][x] == 'E':
            end_position = (x, y)
            lines[y][x] = 'z'


visited = set()

while frontier:
    x, y, steps = frontier.pop(0)
    if (x, y) in visited:
        continue
    visited.add((x, y))
    for dir in dirs:
        new_x, new_y = x + dir[0], y + dir[1]
        if new_x >= 0 and new_y >= 0 and new_x < GRID_WIDTH and new_y < GRID_HEIGHT and (new_x, new_y) not in visited:
            if ord(lines[new_y][new_x]) - ord(lines[y][x]) <= 1:
                if (new_x, new_y) == end_position:
                    print(steps + 1)
                    frontier = []
                    break
                else:
                    frontier.append((new_x, new_y, steps + 1))
