#My inital way
with open('Trees.txt') as file:
    data2 = file.read().split('\n')

def part1(data2, right, down):
    j = 0
    collisions = 0
    for i in range(0, len(data2), down):
        if data2[i][j] == '#':
            collisions +=1
        j = (j+right) % len(data2[0])
    return collisions

print(f'answer for part one 1: {part1(data2, 3, 1)}')


def part2(data2):
    res = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        res *= part1(data2, right, down)
    return res

print(f'answer for part one 2: {part2(data2)}')

#
#
# #Another way of doing it from reddit
# right = 3
# down = 1
# with open('Trees.txt') as file:
#     data = file.readlines()
# treecount = 0
# for i in range(0, len(data), down):
#     if data[i][right * i % len(data[i].strip())] == '#':
#         treecount += 1
#
# print(treecount)
