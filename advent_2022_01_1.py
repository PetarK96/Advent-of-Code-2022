f = open("advent_2022_01_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

lines.append("")

max_elf = 0
current_elf = 0

for line in lines:
    if line:
        current_elf += int(line)
    else:
        max_elf = max(max_elf, current_elf)
        current_elf = 0

print(max_elf)