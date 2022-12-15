f = open("advent_2022_15_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

mds = {}

for line in lines:
    line = line.split(":")
    s, b = line[0].split(), line[1].split()
    sx, sy = int(s[2].split("=")[1][:-1]), int(s[3].split("=")[1])
    bx, by = int(b[4].split("=")[1][:-1]), int(b[5].split("=")[1])
    md = (max(sx, bx) - min(sx, bx)) + (max(sy, by) - min(sy, by))
    mds[(sx, sy)] = md

MAX_X, MAX_Y = 4000000, 4000000
#MAX_X, MAX_Y = 20, 20

x, y = 0, 0

while y <= MAX_Y:
    while x <= MAX_X:
        new_x = x
        for beacon in mds:
            rem = mds[beacon] - (max(beacon[1], y) - min(beacon[1], y))
            if rem < 0:
                continue
            if (beacon[0] - rem) <= x <= (beacon[0] + rem):
                new_x = beacon[0] + rem + 1
                break
        if new_x == x:
            print(x * 4000000 + y)
            exit(0)
        x = new_x
    y += 1
    x = 0