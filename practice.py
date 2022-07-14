import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
dist = [2147483647 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    arr[A].append([B, C])
    arr[B].append([A, C])

H, dist[2], dp[2] = [[0, 2]], 0, 1
while H:
    curD, now = heapq.heappop(H)
    if curD > dist[now]:
        continue
    for next, newD in arr[now]:
        cost = newD + curD
        if cost < dist[next]:
            dist[next] = cost
            heapq.heappush(H, [cost, next])
        if curD > dist[next]:
            dp[now] += dp[next]
print(dp[1])