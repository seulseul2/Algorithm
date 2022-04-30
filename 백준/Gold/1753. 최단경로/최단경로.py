import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

INF = 1e10
distance = [INF] * (V+1)
graph = [[] for _ in range(V+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(x):
    queue = []
    heapq.heappush(queue, [0, x])
    distance[x] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])
dijkstra(start)

for i in range(1, V+1):
    if distance[i] == 1e10:
        print('INF')
    else:
        print(distance[i])