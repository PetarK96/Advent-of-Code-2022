f = open("advent_2022_22_input.txt")
GRID_SIZE = 50
#f = open("test_input.txt")
#GRID_SIZE = 4

lines = [line.strip("\n") for line in f.readlines()]

f.close()

grid = {}

start_spot = None

for y, line in enumerate(lines[:-1]):
    for x, char in enumerate(line):
        if char == " ":
            continue
        else:
            if start_spot is None:
                start_spot = (x + 1, y + 1)
            grid[(x + 1, y + 1)] = char

path = lines[-1]
new_path = []

start_index, end_index = 0, 0
while end_index < len(path):
    if path[end_index] in ('R', 'L'):
        new_path.append(int(path[start_index:end_index]))
        new_path.append(path[end_index])
        start_index, end_index = end_index + 1, end_index + 1
    else:
        end_index += 1

new_path.append(int(path[start_index:end_index]))
path = new_path

faces = 'RDLU'
dirs = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}

def get_side(position):
    if position[1] <= GRID_SIZE:
        if position[0] > GRID_SIZE and position[0] <= (GRID_SIZE * 2):
            return 'A'
        elif position[0] > (GRID_SIZE * 2) and position[0] <= (GRID_SIZE * 3):
            return 'B'
    elif position[1] > GRID_SIZE and position[1] <= (GRID_SIZE * 2):
        return 'C'
    elif position[1] > (GRID_SIZE * 2) and position[1] <= (GRID_SIZE * 3):
        if position[0] <= GRID_SIZE:
            return 'D'
        elif position[0] > GRID_SIZE and position[0] <= (GRID_SIZE * 2):
            return 'E'
    elif position[1] > (GRID_SIZE * 3) and position[1] <= (GRID_SIZE * 4):
        return 'F'

def get_connection(position, side, dir):
    if side == 'A':
        if dir == 'L':
            new_pos = (1, 151 - position[1])
            new_dir = 'R'
        elif dir == 'U':
            new_pos = (1, 100 + position[0])
            new_dir = 'R'
    elif side == 'B':
        if dir == 'U':
            new_pos = (position[0] - 100, 200)
            new_dir = 'U'
        elif dir == 'R':
            new_pos = (100, 151 - position[1])
            new_dir = 'L'
        elif dir == 'D':
            new_pos = (100, position[0] - 50)
            new_dir = 'L'
    elif side == 'C':
        if dir == 'L':
            new_pos = (position[1] - 50, 101)
            new_dir = 'D'
        elif dir == 'R':
            new_pos = (position[1] + 50, 50)
            new_dir = 'U'
    elif side == 'D':
        if dir == 'U':
            new_pos = (51, position[0] + 50)
            new_dir = 'R'
        elif dir == 'L':
            new_pos = (51, 151 - position[1])
            new_dir = 'R'
    elif side == 'E':
        if dir == 'R':
            new_pos = (150, 151 - position[1])
            new_dir = 'L'
        elif dir == 'D':
            new_pos = (50, 100 + position[0])
            new_dir = 'L'
    elif side == 'F':
        if dir == 'L':
            new_pos = (position[1] - 100, 1)
            new_dir = 'D'
        elif dir == 'D':
            new_pos = (position[0] + 100, 1)
            new_dir = 'D'
        elif dir == 'R':
            new_pos = (position[1] - 100, 150)
            new_dir = 'U'

    return (new_pos, new_dir)

connections = {}

for position in grid:
    side = get_side(position)
    for dir in dirs:
        new_position = (position[0] + dirs[dir][0], position[1] + dirs[dir][1])
        if new_position not in grid:
            connections[(position, dir)] = get_connection(position, side, dir)

current_pos = start_spot
facing = 'R'

for instruction in path:
    if instruction == 'R':
        facing = faces[(faces.index(facing) + 1) % 4]
    elif instruction == 'L':
        facing = faces[faces.index(facing) - 1]
    else:
        for _ in range(instruction):
            new_pos = (current_pos[0] + dirs[facing][0], current_pos[1] + dirs[facing][1])
            new_facing = facing
            if new_pos not in grid:
                new_pos, new_facing = connections[(current_pos, facing)]
            if grid[new_pos] == '#':
                break
            else:
                current_pos = new_pos
                facing = new_facing

print(current_pos)
print((1000 * current_pos[1]) + (4 * current_pos[0]) + faces.index(facing))