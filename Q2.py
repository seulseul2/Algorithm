import sys
sys.stdin = open('sample_input (3).txt')

def bfs():
    global level
    Q = [(N-1, 0, 1)]
    visited[N-1][0] = 1
    while Q:
        y, x, lv = Q.pop(0)
        if arr[y][x] == 3:
            if level > lv:
                level = lv
            continue
        if lv > level:
            continue
        for dy, dx in [(0, 1), (0, -1)]:
            if 0 <= x+dx < M and not arr[y][x+dx]:
                if not visited[y][x+dx] or visited[y][x+dx] > lv:
                    visited[y+dy][x+dx] = lv
                    Q.append((y+dy, x+dx, lv))

        for dy in range(1, N):
            if 0 <= y+dy < N and not arr[y+dy][x]:
                if not visited[y + dy][x]:
                    if dy > visited[y][x]:
                        visited[y + dy][x] = dy
                    else:
                        visited[y + dy][x] = visited[y][x]
                    Q.append((y + dy, x, visited[y + dy][x]))
                    break
                elif visited[y + dy][x] > visited[y][x]:
                    visited[y + dy][x] = visited[y][x]
                    Q.append((y + dy, x, visited[y][x]))
                    break

        for dy in range(1, y+1):
            if 0 <= y-dy < N and not arr[y-dy][x]:
                if not visited[y-dy][x]:
                    if dy > visited[y][x]:
                        visited[y - dy][x] = dy
                    else:
                        visited[y - dy][x] = visited[y][x]
                    Q.append((y-dy, x, visited[y-dy][x]))
                    break
                elif visited[y-dy][x] > dy:
                    visited[y-dy][x] = visited[y][x]
                    Q.append((y-dy, x,visited[y-dy][x]))
                    break


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    level = 50
    for i in range(N):
        arr.append(list(map(int, input().split())))
    visited = [[0] * M for _ in range(N)]
    bfs()
    print(level)