def find(cnt, k, s):
    global result
    c_lst[s] = 1
    if k > result:
        return
    if cnt == N-1:
        k += arr[s][0]
        if k > result:
            return
        else:
            result = k
            return
    for i in range(N):
        if c_lst[i] == 0:
            find(cnt+1, k+arr[s][i], i)
            c_lst[i] = 0
    


T = int(input())
for tc in range(1, T+1):
    result = 100000000
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    c_lst = [0] * N
    find(0, 0, 0)
    print(f'#{tc} {result}')
    