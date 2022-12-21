f = open("advent_2022_21_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

done = {}
waiting = {}

for line in lines:
    monkey, rest = line.split(": ")
    rest = rest.split()
    if len(rest) == 1:
        done[monkey] = int(rest[0])
    else:
        waiting[monkey] = rest

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

print(find_value("root"))