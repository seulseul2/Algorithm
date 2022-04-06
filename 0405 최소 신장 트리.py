# 최소 신장트리를 만들고 가중치의 합을 retrun
def prim():
    # 이미 본 vertex를 저장
    #if i not in U:
    U = []
    # 현재 시점의 최선의 상태를 저장
    D = [1e10] * (V+1)
    D[0] = 0
    while len(U) < (V+1):
        #1 현재 상태의 최선의 curV를 구한다.
        minV = 1e10
        for i in range(V+1):
            # 이미 본거는 다시 볼 필요 없으므로
            if i in U:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        #2
        U.append(curV)
        #3 curV로부터 연결된 D를 업데이트한다.
        for i in range(V+1):
            if i in U:
                continue
            if G[curV][i]>0 and D[i] > G[curV][i]:
                D[i] = G[curV][i]
    return sum(D)

T = int(input())
for TC in range(1, T+1):
    V, E = map(int, input().split())
    # 연결이 안되어 있으면 0, 연결되어 있으면 w
    G = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        v1, v2, w = map(int, input().split())
        G[v1][v2] = w
        G[v2][v1] = w

    # print(G)
    print('#{} {}' .format(TC, prim()))