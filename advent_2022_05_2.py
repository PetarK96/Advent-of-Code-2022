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
    # move 2 from 7 to 2
    _, a, _, b, _, c = line.split(" ")
    a, b, c = int(a), int(b), int(c)

    move_crates = crates_dict[b][-a:]
    crates_dict[b] = crates_dict[b][:-a]
    crates_dict[c] += move_crates

ans = ""

for crate in range(1, 10):
    ans += crates_dict[crate][-1]

print(ans)