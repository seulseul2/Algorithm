import sys
input = sys.stdin.readline

N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if maps[j][k]==1 or (maps[j][i]==1 and maps[i][k]==1):
                maps[j][k] = 1

for row in maps:
    print(*row)