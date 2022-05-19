import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 가로축 == 가방의 무게 // 세로축 == 물품
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
stuff = [[0, 0]]

for i in range(N):
    stuff.append(list(map(int, input().split())))

# N은 물품의 수, K는 가방의 최대 무게
# 여기서 i는 i개만큼의 물건을 조합했을 때, 나오는 max무게별 최대 가치
for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = stuff[i]
        # 만약 가방 무게보다, 물품의 무게가 무겁다면
        if j < weight:
            # 물건이 추가되지 않은 무게랑 같다.
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
print(dp[N][K])