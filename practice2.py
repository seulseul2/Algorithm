import sys
input = sys.stdin.readline
N = int(input())

lst = list(map(int, input().split()))
stack = [0]
result = [-1] * N

for i in range(N):
    while stack and lst[i] > lst[stack[-1]]:
        result[stack.pop()] = lst[i]
    stack.append(i)

print(*result)