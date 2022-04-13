def dfs(y, x):
    stack = [[y, x]]
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    while stack:
        cY, cX = stack.pop()
        for i in range(X):
            nY, nX = cY+dY[i], cX+dX[i]
            if 0<=nY<N and 0<=nX<M and maps[nY][nX] != 0 and not visited[nY][nX]:
                if maps[nY][nX] == 3:
                    return True
                stack.append([nY, nX])
                visited[nY][nX] = True
    return False

T = int(input())
for TC in range(1, T+1):
    dY = [0, 0]
    dX = [-1, 1]
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    jump = 0
    X = 2
    while jump < 50:
        jump += 1
        X += 2
        dY.append(jump)
        dY.append(-jump)
        dX.append(0)
        dX.append(0)
        if dfs(N-1, 0):
            print('#{} {}' .format(TC, jump))
            break