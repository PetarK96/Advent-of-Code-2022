f = open("advent_2022_25_input.txt")
#f = open("test_input.txt")

lines = [line.strip("\n") for line in f.readlines()]

f.close()

total = 0

for line in lines:
    power = 0
    for x in line[::-1]:
        total += ("=-012".find(x) - 2) * (5 ** power)
        power += 1

print(total)

snafu = ""

while total:
    rem = total % 5
    total //= 5

    if rem <= 2:
        snafu = str(rem) + snafu
    else:
        snafu = "   =-"[rem] + snafu
        total += 1

print(snafu)
