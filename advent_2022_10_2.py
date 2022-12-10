f = open("advent_2022_10_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

cycle = 0
X = 1

current_row = ['?'] * 40
rows = []

for line in lines:
    for _ in range(1 if line == "noop" else 2):
        cycle += 1
        current_row[cycle - 1] = '#' if cycle - 1 in (X - 1, X, X + 1) else ' '

        if cycle == 40:
            rows.append(current_row)
            current_row = ['#'] * 40
            cycle = 0

    if line != "noop":
        X += int(line.split(" ")[1])

for row in rows:
    print(" ".join(row))
