f = open("advent_2022_06_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

line = lines[0]

window = 14

for i in range(len(line) - window):
    if len(set(line[i:i+window])) == window:
        break

print(i + window)