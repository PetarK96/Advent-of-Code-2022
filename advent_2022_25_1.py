f = open("advent_2022_25_input.txt")
#f = open("test_input.txt")

lines = [line.strip("\n") for line in f.readlines()]

f.close()

total = 0

def get_decimal(line):
    power = 0
    decimal = 0
    for i in range(len(line) - 1, -1, -1):
        if line[i] == '-':
            num = -1
        elif line[i] == '=':
            num = -2
        else:
            num = line[i]
        num = int(num) * (5 ** power)
        decimal += num
        power += 1
    return decimal

for line in lines:    
    total += get_decimal(line)

print(total)

print(get_decimal("2011-=2=-1020-1===-1"))