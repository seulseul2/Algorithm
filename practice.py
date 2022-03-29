import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for i in range(n):
    start, end = map(int, input().split())
    meetings.append([end, start])
meetings.sort()

standard = meetings[0][0]
cnt = 1

for j in meetings[1:]:
    if j[1] >= standard:
        standard = j[0]
        cnt += 1

print(cnt)