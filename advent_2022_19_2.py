f = open("advent_2022_19_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

blueprints = {}

for id, line in enumerate(lines):
    line = line.split(": ")[1].split(".")[:-1]
    blueprints[id] = {}
    for robot in line:
        if robot.startswith(" "):
            robot = robot[1:]
        robot = robot.split()
        if len(robot) == 6:
            blueprints[id][robot[1]] = [(int(robot[4]), robot[5])]
        else:
            blueprints[id][robot[1]] = [(int(robot[4]), robot[5]), (int(robot[7]), robot[8])]

MINUTES = 32

total = 1

for blueprint in blueprints:
    if blueprint >= 3:
        continue

    frontier = [(1, [0, 0, 0, 0], [1, 0, 0, 0])]

    best_score = 0
    best_minutes = {}
    max_ore_cost = max([blueprints[blueprint]["ore"][0][0], blueprints[blueprint]["clay"][0][0], blueprints[blueprint]["obsidian"][0][0], blueprints[blueprint]["geode"][0][0]])
    max_clay_cost = blueprints[blueprint]["obsidian"][1][0]
    max_obsidian_cost = blueprints[blueprint]["geode"][1][0]

    solutions = set()
    m = 0

    while frontier:
        minute, resources, robots = frontier.pop(0)
        resources, robots = resources[::], robots[::]

        #print(minute, resources, robots)

        max_builds_left = (MINUTES - minute)
        max_ore_needed = (max_ore_cost * max_builds_left) - (robots[0] * (max_builds_left - 1))
        max_clay_needed = (max_clay_cost * max_builds_left) - (robots[1] * (max_builds_left - 1))
        max_obsidian_needed = (max_obsidian_cost * max_builds_left) - (robots[2] * (max_builds_left - 1))

        if robots[0] == max_ore_cost:
            if resources[0] > max_ore_cost:
                resources[0] = max_ore_cost
        else:
            if resources[0] > max_ore_needed:
                resources[0] = max_ore_needed

        if robots[1] == max_clay_cost:
            if resources[1] > max_clay_cost:
                resources[1] = max_clay_cost
        else:
            if resources[1] > max_clay_needed:
                resources[1] = max_clay_needed

        if robots[2] == max_obsidian_cost:
            if resources[2] > max_obsidian_cost:
                resources[2] = max_obsidian_cost
        else:
            if resources[2] > max_obsidian_needed:
                resources[2] = max_obsidian_needed

        state = (resources[0], resources[1], resources[2], resources[3], robots[0], robots[1], robots[2], robots[3])

        if state in solutions:
            continue

        solutions.add(state)

        new_resources = []
        for i in range(4):
            new_resources.append(resources[i] + robots[i])

        if minute > m:
            m = minute
            print(m)
        if minute == MINUTES:
            best_score = max(best_score, new_resources[3])
            continue

        if minute in best_minutes:
            if minute > 5 and resources[3] == 0 and best_minutes[minute - 1][0][3] > 0:
                continue
            if minute > 5 and resources[2] == 0 and best_minutes[minute - 1][0][2] > 0:
                continue
            if (best_minutes[minute][0][3] > resources[3] and best_minutes[minute][1][3] > robots[3]) or \
               (best_minutes[minute][0][3] == resources[3] and best_minutes[minute][1][3] > robots[3]) or \
               (best_minutes[minute][0][3] > resources[3] and best_minutes[minute][1][3] == robots[3]):
                continue
           # if (best_minutes[minute][0][3] >= new_resources[3] and best_minutes[minute][1][3] >= robots[3]) and \
           #    ((best_minutes[minute][0][2] > new_resources[2] and best_minutes[minute][1][2] > robots[2]) or \
           #     (best_minutes[minute][0][2] == new_resources[2] and best_minutes[minute][1][2] > robots[2]) or \
           #     (best_minutes[minute][0][2] > new_resources[2] and best_minutes[minute][1][2] == robots[2])):
           #     continue
           # if (best_minutes[minute][0][3] >= new_resources[3] and best_minutes[minute][1][3] >= robots[3]) and \
           #    (best_minutes[minute][0][2] >= new_resources[2] and best_minutes[minute][1][2] >= robots[2]) and \
           #    (best_minutes[minute][0][1] > new_resources[1] and best_minutes[minute][1][1] > robots[1]) and \
           #    (best_minutes[minute][0][0] > new_resources[0] and best_minutes[minute][1][0] > robots[0]):
           #     continue

            if (best_minutes[minute][0][3] >= new_resources[3] and best_minutes[minute][1][3] >= robots[3]) and \
               (best_minutes[minute][0][2] >= new_resources[2] and best_minutes[minute][1][2] >= robots[2]) and \
               (best_minutes[minute][0][1] >= new_resources[1] and best_minutes[minute][1][1] >= robots[1]) and \
               (best_minutes[minute][0][0] >= new_resources[0] and best_minutes[minute][1][0] >= robots[0]):
                continue

            if (resources[3] >= best_minutes[minute][0][3] and robots[3] >= best_minutes[minute][1][3]) and \
               (resources[2] >= best_minutes[minute][0][2] and robots[2] >= best_minutes[minute][1][2]) and \
               (resources[1] >= best_minutes[minute][0][1] and robots[1] >= best_minutes[minute][1][1]) and \
               (resources[0] >= best_minutes[minute][0][0] and robots[0] >= best_minutes[minute][1][0]):
                best_minutes[minute] = (resources, robots)
        else:
            best_minutes[minute] = (resources, robots)

        if resources[0] >= blueprints[blueprint]["geode"][0][0] and resources[2] >= blueprints[blueprint]["geode"][1][0]:
            new_robots = robots[::]
            new_robots[3] += 1
            new_resources_2 = new_resources[::]
            new_resources_2[0] -= blueprints[blueprint]["geode"][0][0]
            new_resources_2[2] -= blueprints[blueprint]["geode"][1][0]
            frontier.append((minute + 1, new_resources_2, new_robots))

        if resources[0] >= blueprints[blueprint]["obsidian"][0][0] and resources[1] >= blueprints[blueprint]["obsidian"][1][0] and robots[2] < max_obsidian_cost:
            new_robots = robots[::]
            new_robots[2] += 1
            new_resources_2 = new_resources[::]
            new_resources_2[0] -= blueprints[blueprint]["obsidian"][0][0]
            new_resources_2[1] -= blueprints[blueprint]["obsidian"][1][0]
            frontier.append((minute + 1, new_resources_2, new_robots))

        if resources[0] >= blueprints[blueprint]["clay"][0][0] and robots[1] < max_clay_cost:
            new_robots = robots[::]
            new_robots[1] += 1
            new_resources_2 = new_resources[::]
            new_resources_2[0] -= blueprints[blueprint]["clay"][0][0]
            frontier.append((minute + 1, new_resources_2, new_robots))
                
        if resources[0] >= blueprints[blueprint]["ore"][0][0] and robots[0] < max_ore_cost:
            new_robots = robots[::]
            new_robots[0] += 1
            new_resources_2 = new_resources[::]
            new_resources_2[0] -= blueprints[blueprint]["ore"][0][0]
            frontier.append((minute + 1, new_resources_2, new_robots))

        frontier.append((minute + 1, new_resources, robots))

    total *= best_score
    print((blueprint + 1), best_score)

print(total)