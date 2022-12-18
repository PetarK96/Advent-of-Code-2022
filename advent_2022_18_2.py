f = open("advent_2022_18_input.txt")
#f = open("test_input.txt")

lines = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]

f.close()

exposed = {}
cubes = {}

min_x, min_y, min_z = 1000, 1000, 1000
max_x, max_y, max_z = 0, 0, 0

for (x, y, z) in lines:
    faces = [((x, y, z), (x + 1, y, z), (x, y + 1, z), (x + 1, y + 1, z))
            ,((x, y, z), (x, y, z + 1), (x, y + 1, z), (x, y + 1, z + 1))
            ,((x, y, z + 1), (x + 1, y, z + 1), (x, y + 1, z + 1), (x + 1, y + 1, z + 1))
            ,((x + 1, y, z), (x + 1, y, z + 1), (x + 1, y + 1, z), (x + 1, y + 1, z + 1))
            ,((x, y, z), (x + 1, y, z), (x, y, z + 1), (x + 1, y, z + 1))
            ,((x, y + 1, z), (x + 1, y + 1, z), (x, y + 1, z + 1), (x + 1, y + 1, z + 1))]

    for face in faces:
        if face in exposed:
            exposed[face] = False
        else:
            exposed[face] = True

    cubes[(x, y, z)] = True
    min_x, min_y, min_z = min(min_x, x), min(min_y, y), min(min_z, z)
    max_x, max_y, max_z = max(max_x, x + 1), max(max_y, y + 1), max(max_z, z + 1)

missing = {}

for x in range(min_x + 1, max_x):
    for y in range(min_y + 1, max_y):
        for z in range(min_z + 1, max_z):
            if (x, y, z) in cubes:
                continue
            else:
                missing[(x, y, z)] = True

def evaluate_cube(cube):
    x1, y1, z1 = cube
    search = [(x1 - 1, y1, z1)
             ,(x1 + 1, y1, z1)
             ,(x1, y1 - 1, z1)
             ,(x1, y1 + 1, z1)
             ,(x1, y1, z1 - 1)
             ,(x1, y1, z1 + 1)]

    for c in search:
        if c not in cubes and c not in missing:
            return 0
        if c in missing:
            if not missing[c]:
                return 0

    return 1

while True:
    change_made = False

    for cube in missing:
        if not missing[cube]:
            continue
        change = evaluate_cube(cube)
        if change == 0:
            missing[cube] = False
            if not change_made:
                change_made = True

    if not change_made:
        break

for cube in missing:
    if not missing[cube]:
        continue
    (x, y, z) = cube
    faces = [((x, y, z), (x + 1, y, z), (x, y + 1, z), (x + 1, y + 1, z))
            ,((x, y, z), (x, y, z + 1), (x, y + 1, z), (x, y + 1, z + 1))
            ,((x, y, z + 1), (x + 1, y, z + 1), (x, y + 1, z + 1), (x + 1, y + 1, z + 1))
            ,((x + 1, y, z), (x + 1, y, z + 1), (x + 1, y + 1, z), (x + 1, y + 1, z + 1))
            ,((x, y, z), (x + 1, y, z), (x, y, z + 1), (x + 1, y, z + 1))
            ,((x, y + 1, z), (x + 1, y + 1, z), (x, y + 1, z + 1), (x + 1, y + 1, z + 1))]

    for face in faces:
        if face in exposed:
            exposed[face] = False

count = 0

for face in exposed:
    if exposed[face]:
        count += 1

print(count)
