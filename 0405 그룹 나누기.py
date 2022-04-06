# 대표자를 찾는 함수
def findSet(x):
    # 만약 x와 p[x]가 다르다면, 같을 때까지 계속해서 부모 노드를 찾아감
    while x != p[x]:
        x = p[x]
    # 부모 노드 반환
    return x

# 대표자와 대표자를 연결하여 하나는 자식 노드로, 하나는 부모 노드로 통합하는 함수
def union(v1, v2):
    p[findSet(v2)] = findSet(v1) # v2에 v1을 넣든, v1에 v2를 넣든 방향성은 관계없다. 다만 findSet을 이용해서 대표값을 찾아 넣어주는 것이 중요함. 

T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    edges = list(map(int, input().split()))

    p = [0] * (N+1)
    # make set 작업 : 배열에 인덱스의 값이 자기 자신이 되도록 + 자기자신이 대표가 되도록. x for x in range(N+1) 해도 괜찮을 듯.
    for i in range(N+1):
        p[i] = i

    for j in range(0, len(edges), 2):
        v1 = edges[j]
        v2 = edges[j+1]
        union(v1, v2)
    
    # print(p)
    cnt = [0] * (N+1)
    for k in range(1, N+1):
        cnt[findSet(k)] = 1

    print('#{} {}' .format(TC, sum(cnt)))