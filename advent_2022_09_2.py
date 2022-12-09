f = open("advent_2022_09_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

visited = set()
visited.add((0, 0))

KNOTS = 10

positions = {}

for i in range(KNOTS):
    positions[i] = [0, 0]

dirs = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}

def calc_tail(knot):
    head_x, head_y = positions[knot - 1][0], positions[knot - 1][1]
    tail_x, tail_y = positions[knot][0], positions[knot][1]

    if tail_x in (head_x - 1, head_x, head_x + 1) and \
       tail_y in (head_y - 1, head_y, head_y + 1):
       pass
    else:
        # Knots are on the same Vertical co-ordinate but 2 positions apart
        if tail_x == head_x:
            tail_y += 1 if head_y > tail_y else -1
        # Knots are on the same Horizontal co-ordinate but 2 positions apart
        elif tail_y == head_y:
            tail_x += 1 if head_x > tail_x else -1
        # Tail needs to move in a diagonal direction
        else:
            tail_x += 1 if head_x > tail_x else -1
            tail_y += 1 if head_y > tail_y else -1

    positions[knot] = [tail_x, tail_y]

    if knot == KNOTS - 1:
        visited.add((tail_x, tail_y))

for line in lines:
    dir, amount = line.split(" ")
    for _ in range(int(amount)):
        positions[0][0] += dirs[dir][0]
        positions[0][1] += dirs[dir][1]
        for i in range(1, KNOTS):
            calc_tail(i)

print(len(visited))
