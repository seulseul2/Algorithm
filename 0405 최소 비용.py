from collections import deque

def bfs():
    queue = deque()
    D = [[1e10] * N for _ in range(N)]
    cX = cY = 0
    queue.append([cY, cX])
    D[cY][cX] = 0
    while queue:
        cY, cX = queue.popleft()
        for dY, dX in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nY = cY + dY
            nX = cX + dX
            if 0<=nY<N and 0<=nX<N:
                diff = max(maps[nY][nX] - maps[cY][cX], 0) + 1
                if D[nY][nX] > D[cY][cX] + diff:
                    # visited를 안 쓰는 대신에 돌아가지 않게 하기 위해서 조건에 맞을 때만 append를 해주어야 합니다!
                    queue.append([nY, nX])
                    D[nY][nX] = D[cY][cX] + diff
    return D[N-1][N-1]

T = int(input())
for TC in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    # 현재 시점에서의 최선 => Memoization에 가까움
    print('#{} {}' .format(TC, bfs()))