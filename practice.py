from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
TREE = [[] for _ in range(V+1)]

for i in range(V):
    x = list(map(int, input().split()))
    idx = 1
    while x[idx] != -1:
        TREE[x[0]].append([x[idx], x[idx+1]])
        idx += 2

print(TREE)

def bfs(s):
    q = deque([[s, 0]])
    visited = [0] * (V)
    visited[s-1] = 1
    result = [0, 0]
    while q:
        now, cnt = q.popleft()
        for j in TREE[now]:
            next, value = j[0], j[1]
            if visited[next-1]==0:
                visited[next-1] = 1
                q.append([next, cnt+value])
                if result[1]<cnt+value:
                    result[0]=next
                    result[1]=cnt+value
    return result

a = bfs(1)
b = bfs(a[0])
print(b[1])