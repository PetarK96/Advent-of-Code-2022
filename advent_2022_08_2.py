f = open("advent_2022_08_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

trees = []

for line in lines:
    trees.append([int(height) for height in line])

GRID_WIDTH = len(trees[0])
GRID_HEIGHT = len(trees)

def is_edge(x, y):
    if (x == 0 or x == GRID_WIDTH - 1) or \
       (y == 0 or y == GRID_HEIGHT - 1):
        return True
    else:
        return False

def is_visible(x, y):
    height = trees[y][x]
    grid_row = trees[y]
    grid_column = [trees[col][x] for col in range(GRID_HEIGHT)]

    if all([t < height for t in grid_row[:x]]) or \
       all([t < height for t in grid_row[x+1:]]) or \
       all([t < height for t in grid_column[:y]]) or \
       all([t < height for t in grid_column[y+1:]]):
        return True
    else:
        return False

def calc_score(x, y):
    height = trees[y][x]
    grid_row = trees[y]
    grid_column = [trees[col][x] for col in range(GRID_HEIGHT)]

    up = calc_direction(grid_column[:y][::-1], height)
    down = calc_direction(grid_column[y+1:], height)
    left = calc_direction(grid_row[:x][::-1], height)
    right = calc_direction(grid_row[x+1:], height)

    return (up * down * left * right)

def calc_direction(subset, height):
    for index, t in enumerate(subset):
        if t >= height:
            break
    return index + 1
  
scenic_score = 0

for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        if is_edge(x, y):
            pass
        else:
            scenic_score = max(scenic_score, calc_score(x, y))

print(scenic_score)
