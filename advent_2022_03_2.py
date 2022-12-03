f = open("advent_2022_03_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

total = 0

for index in range(0, len(lines), 3):
    for char in lines[index]:
        if char in lines[index + 1] and char in lines[index + 2]:
            break

    if ord(char) <= ord('Z'):
        total += (ord(char) - 38)
    else:
        total += (ord(char) - 96)

print(total)