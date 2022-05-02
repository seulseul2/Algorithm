import heapq
import sys
input = sys.stdin.readline

INF = 1e10
dX = [0, 0, -1, 1]
dY = [-1, 1, 0, 0]

def dijkstra():
    queue = []
    minC = [[INF] * N for _ in range(N)]
    minC[0][0] = cave[0][0]
    heapq.heappush(queue, [cave[0][0], [0, 0]])
    while queue:
        money, position = heapq.heappop(queue)
        cY, cX = position[0], position[1]
        if minC[cY][cX] < money:
            continue
        for i in range(4):
            nY = cY + dY[i]
            nX = cX + dX[i]
            if 0<=nY<N and 0<=nX<N:
                cost = money + cave[nY][nX]
                if cost < minC[nY][nX]:
                    minC[nY][nX] = cost
                    heapq.heappush(queue, [cost, [nY, nX]])
    return minC[-1][-1]

TC = 0
while 1:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    TC += 1
    print('Problem {}: {}' .format(TC, dijkstra()))