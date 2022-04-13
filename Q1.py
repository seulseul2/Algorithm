def check(y, x):
    global result
    lst = result[::]
    c_y, c_x = lst[3]
    flag = 0
    visit = []
    if x % 2:
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]:
            if 0 <= y + dy < H and 0 <= x + dx < W and arr[c_y][c_x] < arr[y+dy][x+dx] and not visited[y+dy][x+dx]:
                if not visit:
                    visited[y+dy][x+dx] = 1
                    visit.append((y+dy, x+dx))
                    c_y, c_x = y + dy, x + dx
                else:
                    n_y, n_x = visit.pop()
                    visited[n_y][n_x] = 0
                    visited[y+dy][x+dx] = 1
                    visit.append((y+dy, x+dx))
                    c_y, c_x = y + dy, x + dx
                lst[3] = (y+dy, x+dx)
                flag = 1
    else:
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)]:
            if 0 <= y + dy < H and 0 <= x + dx < W and arr[c_y][c_x] < arr[y+dy][x+dx] and not visited[y+dy][x+dx]:
                if not visit:
                    visited[y+dy][x+dx] = 1
                    visit.append((y+dy, x+dx))
                    c_y, c_x = y+dy, x+dx
                else:
                    n_y, n_x = visit.pop()
                    visited[n_y][n_x] = 0
                    visited[y+dy][x+dx] = 1
                    visit.append((y+dy, x+dx))
                    c_y, c_x = y + dy, x + dx
                lst[3] = (y + dy, x + dx)
                flag = 1
    if flag:
        c_y, c_x = lst[2]
        if x % 2:
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]:
                if 0 <= y + dy < H and 0 <= x + dx < W and arr[c_y][c_x] < arr[y + dy][x + dx] and not visited[y+dy][x+dx]:
                    if len(visit) == 1:
                        visited[y + dy][x + dx] = 1
                        visit.append((y + dy, x + dx))
                        c_y, c_x = y + dy, x + dx
                    else:
                        n_y, n_x = visit.pop()
                        visited[n_y][n_x] = 0
                        visited[y + dy][x + dx] = 1
                        visit.append((y + dy, x + dx))
                        c_y, c_x = y + dy, x + dx
                    lst[2] = (y + dy, x + dx)
        else:
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)]:
                if 0 <= y + dy < H and 0 <= x + dx < W and arr[c_y][c_x] < arr[y + dy][x + dx] and not visited[y+dy][x+dx]:
                    if len(visit) == 1:
                        visited[y + dy][x + dx] = 1
                        visit.append((y + dy, x + dx))
                        c_y, c_x = y + dy, x + dx
                    else:
                        n_y, n_x = visit.pop()
                        visited[n_y][n_x] = 0
                        visited[y + dy][x + dx] = 1
                        visit.append((y + dy, x + dx))
                        c_y, c_x = y + dy, x + dx
                    lst[2] = (y + dy, x + dx)

    for y, x in visit:
        visited[y][x] = 0
    ans = 0
    for y, x in lst:
        ans += arr[y][x]
    return ans, lst



def find():
    global result, maxV, ans_lst
    if len(result) == 4:
        ans = 0
        for c_y, c_x in result:
            ans += arr[c_y][c_x]
        ans1, lst = check(result[0][0], result[0][1])
        if maxV < ans1:
            maxV = ans1
            ans_lst = lst
        return
    y, x = result[-1]
    if x % 2:
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]:
            if 0 <= y+dy < H and 0 <= x+dx < W and not visited[y+dy][x+dx]:
                visited[y+dy][x+dx] = 1
                result.append((y+dy, x+dx))
                find()
                result.pop()
                visited[y+dy][x+dx] = 0
    else:
        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)]:
            if 0 <= y + dy < H and 0 <= x + dx < W and not visited[y + dy][x + dx]:
                visited[y + dy][x + dx] = 1
                result.append((y + dy, x + dx))
                find()
                result.pop()
                visited[y + dy][x + dx] = 0


N = int(input())
for tc in range(1, N+1):
    W, H = map(int, input().split())
    arr = []
    maxV = 0
    ans_lst = []
    visited = [[0] * W for _ in range(H)]
    for i in range(H):
        arr.append(list(map(int, input().split())))
    for i in range(H):
        for j in range(W):
            result = [(i, j)]
            visited[i][j] = 1
            find()
            result.pop()
            visited[i][j] = 0
    print(f'#{tc} {maxV**2}')

