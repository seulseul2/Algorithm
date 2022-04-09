import sys
input = sys.stdin.readline
n = int(input())
maps = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dY = [-1, 1, 0, 0]
dX = [0, 0, -1, 1]

def dfs(y, x):
    standard = maps[y][x]
    stack = [[y, x]]
    visited[y][x] = True
    if maps[y][x] == standard:
                visited[y][x] = True
                stack = [[y, x]]
                while stack:
                    cY, cX = stack.pop()
                    for i in range(4):
                        nY, nX = cY+dY[i], cX+dX[i]
                        if 0<=nY<n and 0<=nX<n and not visited[nY][nX] and maps[nY][nX] == standard:
                            visited[nY][nX] = True
                            stack.append([nY, nX])
c1 = 0

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            c1 += 1
            dfs(y, x)

for y in range(n):
    for x in range(n):
        if maps[y][x] == 'R':
            maps[y][x] = 'G'

visited = [[False] * n for _ in range(n)]
c2 = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            c2 += 1
            dfs(y, x)
print(c1, c2)