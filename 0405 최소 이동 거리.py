# 0에서 N까지의 합이 최소가 되는 경로의 합
def dijk():
    # 이미 본 vertex를 저장
    #if i not in U:
    U = []
    # 현재 시점까지의 최선의 경로의 합 저장
    D = [1e10] * (N+1)
    D[0] = 0
    while len(U) < (N+1):
        #1 현재 상태의 최선의 curV를 구한다.
        minV = 1e10
        for i in range(N+1):
            # 이미 본거는 다시 볼 필요 없으므로
            if i in U:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        #2
        U.append(curV)
        #3 curV로부터 연결된 D를 업데이트한다.
        for i in range(N+1):
            if i in U:
                continue
            if G[curV][i]>0:
                D[i] = min(D[i], D[curV] + G[curV][i])

    return D[N]

T = int(input())
for TC in range(1, T+1):
    N, E = map(int, input().split())
    # 연결이 안되어 있으면 0, 연결되어 있으면 w
    G = [[0] * (N+1) for _ in range(N+1)]

    for i in range(E):
        v1, v2, w = map(int, input().split())
        G[v1][v2] = w
        # G[v2][v1] = w

    # print(G)
    print('#{} {}' .format(TC, dijk()))