f = open("advent_2022_22_input.txt")
#f = open("test_input.txt")

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
            if new_pos not in grid:
                if facing == 'R':
                    new_pos = (sorted([key[0] for key in grid.keys() if key[1] == new_pos[1]])[0], new_pos[1])
                elif facing == 'L':
                    new_pos = (sorted([key[0] for key in grid.keys() if key[1] == new_pos[1]])[-1], new_pos[1])
                elif facing == 'U':
                    new_pos = (new_pos[0], sorted([key[1] for key in grid.keys() if key[0] == new_pos[0]])[-1])
                elif facing == 'D':
                    new_pos = (new_pos[0], sorted([key[1] for key in grid.keys() if key[0] == new_pos[0]])[0])
            if grid[new_pos] == '#':
                break
            else:
                current_pos = new_pos

print(current_pos)
print((1000 * current_pos[1]) + (4 * current_pos[0]) + faces.index(facing))