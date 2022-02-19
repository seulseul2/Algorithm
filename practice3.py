arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# lst = [[0]*5 for _ in range(5)]

# for i in range(n):
#     for j in range(m):
#         for x in range(4):
#             if 0<= j+dx[x] < m and 0 <= i+dy[x] < n:
#                 lst[i][j] += [arr][i+dy[x]][i+dx[x]]

# print(lst)



def myAbs(value):
    if value < 0:
        return value*(-1)
    return value

arr = [list(map(int, input().split())) for _ in range(5)]

sumV = 0
for y in range(5):
    for x in range(5):
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[y]
            sumV += myAbs(arr[ny][nx] - arr[y][x])
print(sumV)