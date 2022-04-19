import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
lst = list(map(int, input().split()))

maxV = -1e10
minV = 1e10

def dfs(depth, total, plus, minus, multiply, divide):
    global maxV, minV
    if depth == N:
        maxV = max(total, maxV)
        minV = min(total, minV)
    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/num[depth]), plus, minus, multiply, divide-1)
dfs(1, num[0], lst[0], lst[1], lst[2], lst[3])
print(maxV)
print(minV)