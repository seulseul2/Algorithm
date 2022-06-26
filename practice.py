from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for data in permutations(lst, M):
    print(*data)