f = open("advent_2022_07_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

dir_sizes = {}

current_dir = ""
current_path = []

for line in lines:
    if line.startswith('$'):
        if line[2:4] == 'cd':
            current_dir = line[5:]
            if current_dir == '..':
                current_dir = current_path[-2]
                current_path.pop()
            else:
                if current_dir == '/':
                    current_path = ['/']
                else:
                    current_dir = current_path[-1] + '/' + current_dir
                    current_path.append(current_dir)

                if current_dir not in dir_sizes:
                    dir_sizes[current_dir] = 0
    else:
        if line.startswith('dir'):
            pass
        else:
            size, _ = line.split(" ")
            for dir in current_path:
                dir_sizes[dir] += int(size)

target = 30000000 - (70000000 - dir_sizes['/'])

best_size = 70000000

for dir in dir_sizes:
    if dir_sizes[dir] > target:
        best_size = min(best_size, dir_sizes[dir])

print(best_size)