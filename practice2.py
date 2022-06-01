import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lsta = list(map(int, input().split()))
lstb = list(map(int, input().split()))
lst = []

idxa = idxb = 0

while idxa<N and idxb<M:
    if lsta[idxa] > lstb[idxb]:
        lst.append(lstb[idxb])
        idxb += 1
    else:
        lst.append(lsta[idxa])
        idxa += 1

if idxa == N:
    while idxb<M:
        lst.append(lstb[idxb])
        idxb += 1
elif idxb == M:
    while idxa<N:
        lst.append(lsta[idxa])
        idxa += 1

print(*lst)