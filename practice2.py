from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001
cnt = 0

def bfs(x):
    global cnt
    standard = 1e10
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        cur = queue.popleft()
        for new in [cur-1, cur+1, cur*2]:
            if 0<=new<=100000:
                
                
                 and not visited[new]:
                visited[new] = visited[cur] + 1
                queue.append(new)
                if new == K:
                    standard = visited[cur] + 1
            if new == K and standard == visited[cur] + 1:
                cnt += 1
    return standard - 1

if N == K:
    print(0)
    print(1)
else:
    print(bfs(N))
    print(cnt)