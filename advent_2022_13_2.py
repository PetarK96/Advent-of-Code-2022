f = open("advent_2022_13_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

right_list = []

def parse_list(text):
    output = []
    text = text[1:-1] + ','
    if text == ",":
        return []
    start = 0
    open_count = 0
    for end, char in enumerate(text):
        if char == '[':
            open_count += 1
        elif char == ']':
            open_count -= 1
        elif char == ',' and open_count == 0:
            subtext = text[start:end]
            open_count = 0
            start = end + 1
            if subtext[0] == '[':
                output.append(parse_list(subtext))
            else:
                output.append(int(subtext))

    return output

def is_right_order(left, right):
    checks = 0
    for pair in zip(left, right):
        checks += 1
        if isinstance(pair[0], int) and isinstance(pair[1], int):
            if pair[0] < pair[1]:
                return 1
            if pair[0] > pair[1]:
                return 0
        else:
            left_list, right_list = pair[0], pair[1]
            if not(isinstance(pair[0], list)):
                left_list = [pair[0]]
            if not(isinstance(pair[1], list)):
                right_list = [pair[1]]

            check = is_right_order(left_list, right_list)
            if check == 1:
                return 1
            if check == 0:
                return 0

    if checks < len(left):
        return 0
    elif checks < len(right):
        return 1
    else:
        return 2

packets = [parse_list(lines[0])]

lines.append("")
lines.append("[[2]]")
lines.append("[[6]]")

for line in lines[1:]:
    found = False
    if line != "":
        line = parse_list(line)
        for index, packet in enumerate(packets):
            if is_right_order(line, packet) == 1:
                packets.insert(index, line)
                found = True
                break
        if not found:
            packets.append(line)

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
