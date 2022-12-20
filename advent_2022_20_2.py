f = open("advent_2022_20_input.txt")
#f = open("test_input.txt")

lines = [int(line.strip()) * 811589153 for line in f.readlines()]

f.close()

LENGTH = len(lines)

positions = list(range(LENGTH))

for _ in range(10):
    for index in range(LENGTH):
        if lines[index] == 0:
            zero_pos = index
            continue

        value = lines[index]

        current_index = positions.index(index)

        new_index = (current_index + value) % (LENGTH - 1)

        positions.pop(current_index)
        positions.insert(new_index, index)

zero_pos = positions.index(zero_pos)

a = lines[positions[(zero_pos + 1000) % (LENGTH)]]
b = lines[positions[(zero_pos + 2000) % (LENGTH)]]
c = lines[positions[(zero_pos + 3000) % (LENGTH)]]

print(a + b + c)