f = open("advent_2022_10_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

cycle = 0
X = 1

strength = 0

current_row = ['#'] * 40

def check_cycle():
    global strength, cycle, current_row
    if cycle == 40:
        strength += (cycle * X)
        print(current_row)
        current_row = ['#'] * 40
        cycle = 0

def place_value():
    value = '#' if cycle - 1 in (X - 1, X, X + 1) else '.'
    current_row[cycle - 1] = value

for line in lines:
    if line == "noop":
        cycle += 1
        place_value()
        check_cycle()
    else:
        _, value = line.split(" ")
        for i in range(2):
            cycle += 1
            place_value()
            check_cycle()
        X += int(value)

print(strength)