import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if maps[i][0] == -1:
        up = i
        down = i+1
        break

dY = [0, 0, -1, 1]
dX = [-1, 1, 0, 0]

def dust():
    tmp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if maps[i][j] != 0 and maps[i][j] != -1:
                minusV = 0
                for k in range(4):
                    nY = i + dY[k]
                    nX = j + dX[k]
                    if 0<=nY<R and 0<=nX<C and maps[nY][nX] != -1:
                        tmp[nY][nX] += maps[i][j]//5
                        minusV += maps[i][j]//5
                maps[i][j] -= minusV
    for i in range(R):
        for j in range(C):
            maps[i][j] += tmp[i][j]

def upclean():
    dY = [-1, 0, 1, 0]
    dX = [0, 1, 0, -1]
    cY = up-1
    cX = 0
    maps[cY][cX] = 0
    direction = 0
    while 1:
        nY, nX = cY+dY[direction], cX+dX[direction]
        if 0<=nY<=up and 0<=nX<C:
            if nY == up and nX == 0:
                maps[cY][cX] = 0
                break
            maps[cY][cX] = maps[nY][nX]
            cY = nY
            cX = nX
            continue
        else:
            direction += 1
            continue

def downclean():
    dY = [1, 0, -1, 0]
    dX = [0, 1, 0, -1]
    cY = down+1
    cX = 0
    maps[cY][cX] = 0
    direction = 0
    while 1:
        nY, nX = cY+dY[direction], cX+dX[direction]
        if down<=nY<R and 0<=nX<C:
            if nY == down and nX == 0:
                maps[cY][cX] = 0
                break
            maps[cY][cX] = maps[nY][nX]
            cY = nY
            cX = nX
            continue
        else:
            direction += 1
            continue

for i in range(T):
    dust()
    upclean()
    downclean()

ans = 0
for i in range(R):
    for j in range(C):
        if maps[i][j] > 0:
            ans += maps[i][j]

print(ans)