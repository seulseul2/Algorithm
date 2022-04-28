import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1e10
maps = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    maps[b].append([a, c])
    maps[a].append([b, c])

def dijkstra(start):
    queue = []
    heapq.heappush(queue, [0, start])
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for j in maps[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(queue, [cost, j[0]])
x, y = map(int, input().split())

dijkstra(1)
A1 = distance[x]
B1 = distance[y]

distance = [INF] * (N+1)
dijkstra(x)
A2 = distance[y]
B3 = distance[N]

distance = [INF] * (N+1)
dijkstra(y)
A3 = distance[N]
B2 = distance[x]

result = min(A1+A2+A3, B1+B2+B3)

if result >= 1e10:
    result = -1

print(result)