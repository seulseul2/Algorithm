import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
for i in range(N):
    sumV = 0
    while sumV < M and i < N:
        sumV += lst[i]
        if sumV == M:
            ans += 1
            break
        i += 1
print(ans)