__15591 MooTuber (Silver)__

```python
import sys
input = sys.stdin.readline

def dfs(s):
    global cnt
    visited = [False] * (N+1)
    visited[s] = True
    stack = [s]
    while stack:
        start = stack.pop()
        for k in usado[start]:
            if not visited[k[0]] and k[1] >= K:
                visited[k[0]] = True
                cnt += 1
                stack.append(k[0])
    return cnt

N, Q = map(int, input().split())
usado = [[] for _ in range(N+1)]
for i in range(N-1):
    p, q, r = map(int, input().split())
    usado[p].append([q, r])
    usado[q].append([p, r])

for j in range(Q):
    K, V = map(int, input().split())
    cnt = 0
    print(dfs(V))
```