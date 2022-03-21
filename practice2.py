import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int, input().split())
wod = list(map(int, input().split()))
cnt = 0

for i in permutations(wod, n):
    weight = 500
    flag = 1
    for j in i:
        weight += j-k
        if weight < 500:
            flag = 0
            break
    if flag:
        cnt += 1

print(cnt)