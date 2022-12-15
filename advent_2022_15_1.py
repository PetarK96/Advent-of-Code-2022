f = open("advent_2022_15_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

sensors = []
beacons = []

for line in lines:
    line = line.split(":")
    s, b = line[0].split(), line[1].split()
    sensors.append((int(s[2].split("=")[1][:-1]), int(s[3].split("=")[1])))
    beacons.append((int(b[4].split("=")[1][:-1]), int(b[5].split("=")[1])))

Y = 2000000
#Y = 10

exists = set()

for (sx, sy), (bx, by) in zip(sensors, beacons):
    md = (max(sx, bx) - min(sx, bx)) + (max(sy, by) - min(sy, by))
    if (sy - md) <= Y <= (sy + md):
        rem = md - (max(sy, Y) - min(sy, Y))
        for x in range(sx - rem, sx + rem + 1):
            exists.add(x)

for b in beacons:
    if b[1] == Y and b[0] in exists:
        exists.remove(b[0])

print(len(exists))