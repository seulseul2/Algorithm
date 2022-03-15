import sys

sys.stdin = open('input (6).txt')

delX = [-1, 1, 0, 0]
delY = [0, 0, -1, 1]

def dfs(y, x):
    stack = [[y, x]]
    visited = [[False] * 16 for _ in range(16)]
    visited[y][x] = True

    while stack:
        start = stack.pop()
        for j in range(4):
            newX = start[1] + delX[j]
            newY = start[0] + delY[j]
            if 0<=newX<16 and 0<=newY<16:
                if maps[newY][newX] == '3':
                    return 1
                elif not visited[newY][newX] and maps[newY][newX] == '0':
                    stack.append([newY, newX])
                    visited[newY][newX] = True
    return 0

for TC in range(1, 11):
    meaningless = int(input())
    maps = [list(input()) for _ in range(16)]

    for i in range(16):
        if '2' in maps[i]:
            start_y = i
            start_x = maps[i].index('2')
            break
    print('#{} {}' .format(TC, dfs(start_y, start_x)))