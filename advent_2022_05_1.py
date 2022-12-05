f = open("advent_2022_05_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

crates_dict = { 1: ['H', 'T', 'Z', 'D']
              , 2: ['Q', 'R', 'W', 'T', 'G', 'C', 'S']
              , 3: ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H']
              , 4: ['L', 'C', 'N', 'F', 'H', 'Z']
              , 5: ['G', 'L', 'F', 'Q', 'S']
              , 6: ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S']
              , 7: ['Z', 'F', 'J']
              , 8: ['D', 'L', 'V', 'Z', 'R', 'H', 'Q']
              , 9: ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D'] }

for line in lines:
    _, a, _, b, _, c = line.split(" ")
    a, b, c = int(a), int(b), int(c)

    for _ in range (a):
        crate = crates_dict[b].pop()
        crates_dict[c].append(crate)

ans = ""

for crate in range(1, 10):
    ans += crates_dict[crate][-1]

print(ans)