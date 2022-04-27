import sys
import heapq
input = sys.stdin.readline

INF = 1e10
n, m = map(int, input().split())
# 각 노드별 (연결 노드, 거리) 삽입용 초기화
graph = [[] for _ in range(n + 1)]
# 시작 지점에서 각 노드별 최소 거리용 초기화
distance = [INF] * (n + 1)

# 그래프에 (연결된 노드, 거리) 삽입
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    # 최소힙 생성용
    queue = []
    # 최소힙에 (시작점까지 거리=당연히0, 시작점) 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        # 최소거리가 더 작다면, 더 계산할 필요 X
        if distance[now] < dist:
            continue
        # now에서 (연결된 노드, 최소 거리)를 반복
        for i in graph[now]:
            # dist = 여기까지 오는 데 최소 거리 // cost = 연결된 노드들과 최소 거리
            cost = dist + i[1]
            # 만약 연결된 노드들과 최소 거리가 기존 최소거리보다 작다면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 또한, 해당 노드와 연결된 노드들의 거리가 줄어들 수 있기 때문에 재계산을 해줘야함 -> queue에 추가
                heapq.heappush(queue, (cost, i[0]))


dijkstra(1)

# 마지막 지점이 최종 목적지이기 때문에 distance[-1]을 출력
print(distance[-1])