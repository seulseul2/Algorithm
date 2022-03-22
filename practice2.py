import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [x for x in range(1, N+1)]

for data in permutations(lst, M):
    print(*data)