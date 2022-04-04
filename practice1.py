from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
for _ in range(n):
    tmp = list(input().rstrip())
    maps.append(list(map(int, tmp)))

dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1

    while queue:
        x, y, w = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]
        for i in range(4):
            nx = x + dX[i]
            ny = y + dY[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 현재 위치로 이동할 수 있고, 아직 방문하지 않았다면
                if maps[nx][ny] == 0 and not visited[nx][ny][w]:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])
                # 현재 위치가 벽이고, 벽을 아직 부수지 않았다면
                elif maps[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    queue.append([nx, ny, w + 1])
    return -1
print(bfs())