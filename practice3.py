import sys
input = sys.stdin.readline
from collections import deque

# 위쪽 물고기(1순위) # 왼쪽 물고기(2순위)
dX = [0, -1, 1, 0]
dY = [-1, 0, 0, 1]

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
size = 2
size_cnt = 0
time = 0

# 시작점 찾기
for i in range(n):
    if 9 in maps[i]:
        start_y = i
        start_x = maps[i].index(9)
# 아기상어 위치는 0으로 초기화
maps[start_y][start_x] = 0

def bfs(y, x):
    global size
    global size_cnt
    global time
    minD = 1e10
    fish_lst = []
    queue = deque()
    queue.append([y, x])
    visited = [[0] * n for _ in range(n)]
    visited[y][x] = 1
    while queue:
        curY, curX = queue.popleft()
        for i in range(4):
            newY = curY + dY[i]
            newX = curX + dX[i]
            # newY와 newX가 범위 안이고, 해당 위치 물고기 사이즈가 같거나 작으며, 방문하지 않았다면
            if 0<=newY<n and 0<=newX<n and maps[newY][newX] <= size and not visited[newY][newX]:
                visited[newY][newX] = visited[curY][curX] + 1
                queue.append([newY, newX])
                # 만약 해당 위치에 물고기가 있다면?
                if 0<maps[newY][newX]<size and visited[newY][newX] <= minD:
                    minD = visited[newY][newX]
                    fish_lst.append([newY, newX])
                elif visited[newY][newX] > minD and fish_lst:
                    fish_lst.sort()
                    newY, newX = fish_lst.pop(0)
                    size_cnt += 1
                    maps[newY][newX] = 0
                    # 사이즈만큼 먹어주었다면 upgrade
                    if size_cnt == size:
                        size_cnt = 0
                        size += 1
                    time += visited[newY][newX] - 1
                    bfs(newY, newX)
    return time

print(bfs(start_y, start_x))