import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 1e10
maps = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(M):
    a, b, c = map(int, input().split())
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
s, e = map(int, input().split())
dijkstra(s)
print(distance[e])