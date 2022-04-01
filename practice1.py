from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        cur = queue.popleft()
        if cur == K:
            return visited[cur]-1
        for i in range(3):
            if i == 0:
                new = cur-1
            elif i == 1:
                new = cur+1
            else:
                new = cur*2
            if new == K:
                return visited[cur]
            elif 0<=new<=100000 and not visited[new]:
                visited[new] = visited[cur] + 1
                queue.append(new)
    return 0

N, K = map(int, input().split())
visited = [0] * 100001
print(bfs(N))