f = open("advent_2022_10_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

cycle = 0
X = 1

ranges = (20, 60, 100, 140, 180, 220)
strength = 0

def check_cycle():
    global strength
    if cycle in ranges:
        strength += (cycle * X)

for line in lines:
    if line == "noop":
        cycle += 1
        check_cycle()
    else:
        _, value = line.split(" ")
        for i in range(2):
            cycle += 1
            check_cycle()
        X += int(value)

print(strength)