import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


# 핵심.
# for j in range(1, N+1):
#     arr[j].sort()

print(arr)
# def dfs(s):
#     stack = [s]
#     visited = [False] * (N+1)
#     lst = []
#     while stack:
#         start = stack.pop()
#         if not visited[start]:
#             visited[start] = True
#             lst.append(start)
#             for e in arr[start][::-1]:
#                 if not visited[e]:
#                     stack.append(e)
#     return lst

# def bfs(s):
#     queue = [s]
#     visited = [False] * (N+1)
#     result = []
#     while queue:
#         start = queue.pop(0)
#         if not visited[start]:
#             visited[start] = True
#             result.append(start)
#             for e in arr[start]:
#                 if not visited[e]:
#                     queue.append(e)
#     return result

# print(*dfs(V))
# print(*bfs(V))