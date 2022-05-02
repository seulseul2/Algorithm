from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        cX, cY = queue.popleft()
        if abs(cX-fest[0]) + abs(cY-fest[1]) <= 1000:
            return 'happy'
        for j in range(n):
            if not visited[j]:
                nX, nY = store[j]
                if abs(cX-nX) + abs(cY-nY) <= 1000:
                    queue.append(store[j])
                    visited[j] = True
    return 'sad'

T = int(input())
for TC in range(T):
    n = int(input())
    home = list(map(int, input().split()))
    store = []
    for i in range(n):
        x, y = map(int, input().split())
        store.append([x, y])
    fest = list(map(int, input().split()))
    visited = [False] * n
    print(bfs(home[0], home[1]))