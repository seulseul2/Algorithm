import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, K+1):
        if i>=coin:
            dp[i] += dp[i-coin]
print(dp[K])