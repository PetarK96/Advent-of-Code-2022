f = open("advent_2022_16_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

valves = {}
all_open = set()

bests = {}
best_steps = {}

for line in lines:
    a, b = line.split(";")
    a, b = a.split(), b.split()
    rate = int(a[4].split("=")[1])
    connections = [v.strip(",") for v in b[4:]]
    valves[a[1]] = (rate, connections)
    bests[a[1]] = {}
    if rate != 0:
        all_open.add(a[1])

frontier = [("AA", {}, 1, 0, 0, ["AA"])]

best_pressure = 0

while frontier:
    valve, open, minute, fpm, total, path = frontier.pop()
    open = set(open)
    new_path = path[::]

    total += fpm
    #print(valve, open, minute, fpm, total, path)

    if minute in bests[valve]:
        if fpm < bests[valve][minute][0] and total < bests[valve][minute][1]:
            continue
        else:
            bests[valve][minute] = (fpm, total)
    else:
        bests[valve][minute] = (fpm, total)

    minute += 1

    if minute == 31:
        best_pressure = max(best_pressure, total)
        continue
    else:
        if open == all_open:
            frontier.append((valve, open, minute, fpm, total, new_path + [valve]))
        else:
            for v in valves[valve][1]:
                frontier.append((v, open, minute, fpm, total, new_path + [v]))
            
            if valve not in open and valves[valve][0] != 0:
                s = set(open)
                s.add(valve)
                frontier.append((valve, s, minute, fpm + valves[valve][0], total, new_path + [valve]))
            
            

print(best_pressure)