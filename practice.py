import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
dp = [0]

tmp = 0
for i in lst:
    tmp += i
    dp.append(tmp)

for i in range(M):
    start, end = map(int, input().split())
    print(dp[end] - dp[start-1])