# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# lst = []

# def btrk(x):
#     if len(lst) == M:
#         print(' '.join(map(str, lst)))
#         return
#     for i in range(x, N+1):
#         lst.append(i)
#         btrk(i)
#         lst.pop()

# btrk(1)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []

def btrk(x):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(x, N+1):
        lst.append(i)
        btrk(i)
        lst.pop()

btrk(1)