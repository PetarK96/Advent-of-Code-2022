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

positions = {}

def get_state():
    state = []
    for x in range(1, 8):
        for y in range(height, height - 50, -1):
            if (x, y) in exists:
                state.append((x, y - height + 50))
    return sorted(state)

found = False
double_found = False
triple_found = False
found_current = ()
found_state = []

shapes = 0

while not triple_found:
    if shapes == 3160:
        print("Height: " + str(height))
    shapes += 1
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

            if height > 100:
                state = get_state()
                current = (shape_index, jets_index, movement)
                if current in positions:
                    for states in positions[current]:
                        if not triple_found and ((not found and state == states) or (found and current == found_current and state == found_state)):
                            print(current)
                            print(state)
                            print(height)
                            print(shapes)
                            if not found:
                                found_current = current
                                found_state = state
                                found = True
                            else:
                                if not double_found:
                                    double_found = True
                                else:
                                    triple_found = True
                else:
                    if not found:
                        positions[current] = []
                if not found:
                    positions[current].append(state)
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