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

frontier = [("AA", "AA", {}, 1, 0, 0, [("AA", "AA")])]

el = ["AA", "YX", "CJ", "XM", "XM", "NR", "UG", "UG", "TI", "GI", "GI", "TI", "UG", "NR", "XM"]
m = ['AA', 'VO', 'YR', 'YR', 'FY', 'QS', 'QW', 'QW', 'KK', 'OO', 'OO', 'HD', 'JB', 'JB', 'UD', 'CA', 'CA', 'AP', 'DW', 'DW', 'PK', 'DZ', 'DZ', 'BA', 'BH', 'BH']

while frontier:
    you, elephant, open, minute, fpm, total, path = frontier.pop()
    open = set(open)
    new_path = path[::]

    
    if minute <= len(el):
        if elephant != el[minute - 1]:
            continue

    if minute <= len(m):
        if you != m[minute - 1]:
            continue

    total += fpm

    if minute in best_steps:
        if total <= best_steps[minute]:
            continue
        else:
            if open == all_open:
                best_steps[minute] = total
    else:
        if open == all_open:
            best_steps[minute] = total

    if (you, elephant) in bests:
        if minute in bests[(you, elephant)]:
            if fpm < bests[(you, elephant)][minute][0] and total < bests[(you, elephant)][minute][1]:
                continue
            else:
                bests[(you, elephant)][minute] = (fpm, total)
        else:
            bests[(you, elephant)][minute] = (fpm, total)
    else:
        bests[(you, elephant)] = {}

    minute += 1

    if minute == 27:
        best_pressure = max(best_pressure, total)
        continue
    else:
        if open == all_open:
            frontier.append((you, elephant, open, minute, fpm, total, new_path + [(you, elephant)]))
        else:
            for y in valves[you][1]:
                for e in valves[elephant][1]:
                    if y != e:
                        frontier.append((y, e, open, minute, fpm, total, new_path + [(y, e)]))
            
            if (you not in open and valves[you][0] != 0) and (elephant not in open and valves[elephant][0] != 0) and (you != elephant):
                s = set(open)
                s.add(you)
                s.add(elephant)
                frontier.append((you, elephant, s, minute, fpm + valves[you][0] + valves[elephant][0], total, new_path + [(you, elephant)]))
            else:
                s2 = set(open)
                if you not in open and valves[you][0] != 0:
                    s2.add(you)
                    for e in valves[elephant][1]:
                        frontier.append((you, e, s2, minute, fpm + valves[you][0], total, new_path + [(you, e)]))
                elif elephant not in open and valves[elephant][0] != 0:
                    s2.add(elephant)
                    for y in valves[you][1]:
                        frontier.append((y, elephant, s2, minute, fpm + valves[elephant][0], total, new_path + [(y, elephant)]))

print(best_pressure)