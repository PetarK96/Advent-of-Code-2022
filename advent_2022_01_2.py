f = open("advent_2022_01_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

lines.append("")

elf_counts = []
current_elf = 0

import bisect

for line in lines:
    if line:
        current_elf += int(line)
    else:
        bisect.insort(elf_counts, current_elf)
        current_elf = 0

print(sum([x for x in elf_counts[-3:]]))