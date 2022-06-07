import sys
input = sys.stdin.readline

N = int(input())
minV = abs(100-N)
M = int(input())
if M:
    broken = list(input().split())
else:
    broken = []

for num in range(1000001):
    for tmp in str(num):
        if tmp in broken:
            break
    else:
        minV = min(minV, len(str(num))+abs(num-N))
print(num)
print(minV)