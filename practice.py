import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
start, end = 0, ((10**5)*20)+1

while start <= end:
    middle = (start+end)//2
    cnt = 0
    score = 0
    for i in lst:
        score += i
        if score >= middle:
            cnt += 1
            score = 0
    if cnt < K:
        end = middle-1
    else:
        start = middle+1

print(start-1)