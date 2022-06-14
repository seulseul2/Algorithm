from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
snake_ladder = dict()

for i in range(N):
    a, b = map(int, input().split())
    snake_ladder[a] = b

for j in range(M):
    a, b = map(int, input().split())
    snake_ladder[a] = b

def bfs():
    q = deque([1])
    visited = [0] * 101
    while q:
        curP = q.popleft()
        if curP == 100:
            return visited[curP]
        for i in range(1, 7):
            newP = curP + i
            if newP<=100 and not visited[newP]:
                visited[newP] = visited[curP] + 1
                if newP in snake_ladder.keys():
                    next = snake_ladder[newP]
                    if not visited[next]:
                        visited[next] = visited[curP] + 1
                        q.append(next)
                else:
                    q.append(newP)
    return 0

print(bfs())