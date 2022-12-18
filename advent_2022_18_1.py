f = open("advent_2022_18_input.txt")
#f = open("test_input.txt")

lines = [[int(x) for x in line.strip().split(",")] for line in f.readlines()]

f.close()

exposed = {}

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

count = 0

for face in exposed:
    if exposed[face]:
        count += 1

print(count)