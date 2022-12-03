f = open("advent_2022_03_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

total = 0

for line in lines:
    p1, p2 = line[:len(line) // 2], line[len(line) // 2:]

    for char in p1:
        if char in p2:
            break

    if ord(char) <= ord('Z'):
        total += (ord(char) - 38)
    else:
        total += (ord(char) - 96)

print(total)