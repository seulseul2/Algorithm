import sys
input = sys.stdin.readline

n = int(input())
x1 = y1 = 1e10
top_down = 0
bottom_up = 0

for i in range(n):
    a, b = map(int, input().split())
    if a > standard_x and b < standard_y:
        top_down += 1
    elif a < 