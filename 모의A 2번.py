import heapq
import sys
input = sys.stdin.readline

N = int(input())
card = []
for i in range(N):
    heapq.heappush(card, int(input()))

total = 0
for j in range(N-1):
    x = heapq.heappop(card) + heapq.heappop(card)
    heapq.heappush(card, x)
    total += x

print(total)