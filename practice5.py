dY = [-1, 0, 1, 0]
dX = [0, 1, 0, -1]

def find(Y, X):
    global direction
    visited = [[0] * M for _ in range(N)]
    visited[Y][X] = 1
    while 1:
        Y += dY[direction]
        X += dX[direction]
        if Y<0 or Y>=N or X<0 or X>=M:
            return False
        visited[Y][X] += 1
        if visited[Y][X] == 10:
            return False
        if maps[Y][X] == 'G':
            return True
        elif maps[Y][X] == '\\':
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1
            else:
                direction = 0
        elif maps[Y][X] == '/':
            if direction == 0:
                direction = 1
            elif direction == 1:
                direction = 0
            elif direction == 2:
                direction = 3
            else:
                direction = 2
        elif maps[Y][X] == 'ㅡ':
            if direction == 0:
                direction = 2
            elif direction == 2:
                direction = 0
        elif maps[Y][X] == 'ㅣ':
            if direction == 1:
                direction = 3
            elif direction == 3:
                direction = 1

M, N = map(int, input().split())
maps = [list(input()) for _ in range(N)]
# 시작점 찾기
for i in range(N):
    for j in range(M):
        if maps[i][j] == '1' or maps[i][j] == '0' or maps[i][j] == '2' or maps[i][j] == '3':
            sY, sX = i, j
            direction = int(maps[i][j])
            break

print(find(sY, sX))