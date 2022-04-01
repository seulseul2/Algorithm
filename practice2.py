# 재귀문
def dfs1(v):
    visited[v] = True
    print(v)
    for w in GL[v]:
        if not visited[w]:
            dfs1(w)

# 반복문으로
def dfs2(v):
    stack = []
    stack.append(v)
    visited[v] = True
    while stack:
        v = stack.pop(-1)
        print(v)
        for w in GL[v]:
            if not visited[w]:
                visited[w] = True
                stack.append(w)

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = 7
visited = [False] * (N+1)
GL = [[] for _ in range(N+1)]
GA = [[0] * (N+1) for _ in range(N+1)]
for i in range(0, len(lst), 2):
    p1 = lst[i]
    p2 = lst[i+1]
    GL[p1].append(p2)
    GL[p2].append(p1)
    GA[p1][p2] = 1
    GA[p2][p1] = 1