f = open("advent_2022_21_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

import copy

done = {}
waiting = {}

for line in lines:
    monkey, rest = line.split(": ")
    rest = rest.split()
    if len(rest) == 1:
        done[monkey] = int(rest[0])
    else:
        waiting[monkey] = rest

done_copy = copy.deepcopy(done)
waiting_copy = copy.deepcopy(waiting)

def find_value(monkey_name):
    if monkey_name in done:
        return done[monkey_name]
    else:
        m1, operator, m2 = waiting[monkey_name]
        m1_value = find_value(m1)
        m2_value = find_value(m2)
        done[m1] = m1_value
        done[m2] = m2_value
        return eval(str(m1_value) + operator + str(m2_value))

tests = {}

for i in range(5):
    done["humn"] = i
    v1 = find_value(waiting["root"][0])
    done = copy.deepcopy(done_copy)
    waiting = copy.deepcopy(waiting_copy)

    done["humn"] = i
    v2 = find_value(waiting["root"][2])
    done = copy.deepcopy(done_copy)
    waiting = copy.deepcopy(waiting_copy)

    tests[i] = (v1, v2)

for test in tests:
    print(test, ": ", tests[test])

difference = 100
span = 3

result = (abs(tests[0][0] - tests[0][1]) // difference) * span
print(int(result))