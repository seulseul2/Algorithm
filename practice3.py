def btrk(employee):
    global pct, max_pct
    # 전체 직원을 다 확인했을 때
    if employee == n:
        if pct > max_pct:
            max_pct = pct
            return

    # 더이상 유망하지 않을 때
    if pct <= max_pct:
        return

    for i in range(n):
        if not visited[i] and ppp[employee][i] != 0:
            visited[i] = 1
            pct *= ppp[employee][i] / 100
            btrk(employee+1)
            visited[i] = 0
            pct /= ppp[employee][i] / 100


T = int(input())
for TC in range(1, T+1):
    n = int(input())
    ppp = [list(map(int, input().split())) for _ in range(n)]
    max_pct = 0.0
    pct = 1.0
    visited = [0] * n
    btrk(0)
    print('#{} {:.6f}' .format(TC, max_pct*100))