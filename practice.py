import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    minV = int(1e9)
    j = 1
    while j**2 <= i:
        minV = min(minV, dp[i-j**2])
        j += 1
    dp.append(minV+1)
print(dp[n])