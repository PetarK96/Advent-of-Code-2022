f = open("advent_2022_09_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

visited = set()

visited.add((0, 0))

head = [0, 0]
tail = [0, 0]

dirs = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}

def calc_tail(dir):
    head_x, head_y = head[0], head[1]
    if tail[0] in (head_x - 1, head_x, head_x + 1) and \
       tail[1] in (head_y - 1, head_y, head_y + 1):
       pass
    else:
        if tail[0] == head_x:
            tail[1] += dirs[dir][1]
        elif tail[1] == head_y:
            tail[0] += dirs[dir][0]
        else:
            if head_x > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1
            
            if head_y > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1

    visited.add((tail[0], tail[1]))

for line in lines:
    dir, amount = line.split(" ")
    for _ in range(int(amount)):
        head[0] += dirs[dir][0]
        head[1] += dirs[dir][1]
        calc_tail(dir)

print(len(visited))