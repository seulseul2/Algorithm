import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int, input().split())
wod = list(map(int, input().split()))
cnt = 0

for data in permutations(wod, n):
    weight = 500
    flag = True
    for i in range(n):
        weight += data[i]
        weight -= k
        if weight < 500:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)