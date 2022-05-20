import sys
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
line = [0] * N

for i in range(N):
    standard = people[i]
    cnt = 0
    for j in range(N):
        if line[j] == 0:
            if cnt == standard:
                line[j] = i+1
                break
            cnt += 1
print(*line)