import sys
input = sys.stdin.readline

lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
T = int(input())
for TC in range(T):
    cnt = 9
    n = int(input())
    while n-1 > cnt:
        lst.append(lst[-1]+lst[-5])
        cnt += 1
    print(lst[n-1])