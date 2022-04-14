import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
maps = [[0] * M for _ in range(N)]
maps[0][0] = 1
a = 1
if K != 0:
    Ky = (K-1)//M
    Kx = (K-1) % M
    for i in range(Ky+1):
        for j in range(Kx+1):
            if i == 0 or j == 0:
                maps[i][j] = 1
            else:
                maps[i][j] = maps[i-1][j] + maps[i][j-1]
    a, maps[Ky][Kx] = maps[Ky][Kx], a
    for i in range(Ky, N):
        for j in range(Kx, M):
            if i == Ky or j == Kx:
                maps[i][j] = 1
            else:
                maps[i][j] = maps[i-1][j] + maps[i][j-1]
    b = maps[N-1][M-1]
else:
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0:
                maps[i][j] = 1
            else:
                maps[i][j] += maps[i-1][j] + maps[i][j-1]
b = maps[N-1][M-1]
print(a*b)