import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 0
minV = 100001
sumV = lst[0]

while 1:
    if sumV >= S:
        sumV -= lst[left]
        minV = min(minV, right-left+1)
        left += 1
    else:
        right += 1
        if right == N:
            break
        sumV += lst[right]

print(0) if minV == 100001 else print(minV)