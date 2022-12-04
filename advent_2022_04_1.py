f = open("advent_2022_04_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

count = 0

for line in lines:
    p1, p2 = line.split(',')
    p1 = p1.split('-')
    p2 = p2.split('-')

    set1 = set(range(int(p1[0]), int(p1[1]) + 1))
    set2 = set(range(int(p2[0]), int(p2[1]) + 1))

    if len(set1.difference(set2)) == 0 or len(set2.difference(set1)) == 0:
        count += 1

print(count)