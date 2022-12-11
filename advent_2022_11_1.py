f = open("advent_2022_11_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

items, operations, tests, true_tests, false_tests = [], [], [], [], []

for line in lines:
    if line.startswith('Starting items'):
        items.append([int(x) for x in line[16:].split(", ")])
    elif line.startswith('Operation'):
        operations.append([x for x in line[11:].split()])
    elif line.startswith('Test'):
        tests.append(int(line[6:].split()[2]))
    elif line.startswith('If true'):
        true_tests.append(int(line[9:].split()[3]))
    elif line.startswith('If false'):
        false_tests.append(int(line[10:].split()[3]))

ROUNDS = 20
MONKEYS = len(items)

monkey_inspections = [0] * MONKEYS

for round in range(ROUNDS):
    for monkey in range(MONKEYS):
        for _ in range(len(items[monkey])):
            worry_level = items[monkey].pop(0)

            increase = operations[monkey][4]
            increase = worry_level if increase == 'old' else int(increase)
            worry_level = worry_level * increase if operations[monkey][3] == '*' else worry_level + increase

            worry_level //= 3

            if worry_level % tests[monkey] == 0:
                items[true_tests[monkey]].append(worry_level)
            else:
                items[false_tests[monkey]].append(worry_level)

            monkey_inspections[monkey] += 1

monkey_inspections = sorted(monkey_inspections)
print(monkey_inspections)
print(monkey_inspections[-1] * monkey_inspections[-2])