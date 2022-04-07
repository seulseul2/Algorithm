import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
Dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if lst[j] > lst[i]:
            Dp[i] = max(Dp[i], Dp[j] + 1)
print(max(Dp))