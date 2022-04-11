import sys
input = sys.stdin.readline

N = int(input())
lst = [0, 1, 1, 2, 3, 5, 8]

if N <= 6:
    print(lst[N])
else:
    cnt = 6
    while cnt < N:
        lst.append(lst[-2]+lst[-1])
        cnt += 1
    print(lst[-1])