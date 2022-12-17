f = open("advent_2022_17_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

jets = lines[0]

shape_dims = [(4, 1), (3, 3), (3, 3), (1, 4), (2, 2)]
shape_points = [((0, 0), (1, 0), (2, 0), (3, 0)), ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)), ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)), ((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (1, 0), (0, 1), (1, 1))]
shape_index = 0
jets_index = 0
JETS_LEN = len(jets)

height = 0

exists = set()

for _ in range(2022):
    shape_bottom = height + 4
    shape_x = 3
    for movement in range(7):
        if movement & 1 == 0:
            jet = jets[jets_index]

            if jet == '<' and shape_x > 1:
                shape_x -= 1
            elif jet == '>' and (shape_x + shape_dims[shape_index][0] - 1) < 7:
                shape_x += 1

            jets_index = 0 if jets_index == JETS_LEN - 1 else jets_index + 1
        else:
            shape_bottom -= 1

    bottom_hit = False

    while True:
        for points in shape_points[shape_index]:
            if (points[0] + shape_x, points[1] + shape_bottom - 1) in exists or shape_bottom - 1 == 0:
                bottom_hit = True
                break

        if bottom_hit:
            break

        shape_bottom -= 1

        jet = jets[jets_index]

        if jet == '<' and shape_x > 1:
            can_move = True
            for points in shape_points[shape_index]:
                if (points[0] + shape_x - 1, points[1] + shape_bottom) in exists:
                    can_move = False
                    break
            if can_move:
                shape_x -= 1
        elif jet == '>' and (shape_x + shape_dims[shape_index][0] - 1) < 7:
            can_move = True
            for points in shape_points[shape_index]:
                if (points[0] + shape_x + 1, points[1] + shape_bottom) in exists:
                    can_move = False
                    break
            if can_move:
                shape_x += 1

        jets_index = 0 if jets_index == JETS_LEN - 1 else jets_index + 1

    for points in shape_points[shape_index]:
        exists.add((points[0] + shape_x, points[1] + shape_bottom))
        height = max(height, points[1] + shape_bottom)

    shape_index = 0 if shape_index == 4 else shape_index + 1

print(height)
#print(exists)