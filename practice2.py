import sys
input = sys.stdin.readline

# 3월 1일 ~ 11월 30일까지 // 60 <= X <= 334
month = {'1': 0, '2':31, '3':59, '4':90, '5':120, '6':151, '7':181, '8':212, '9':243, '10':273, '11':304, '12':334}

N = int(input())
flowers = []
for i in range(N):
    flower = list(input().split())
    start = month[flower[0]] + int(flower[1])
    end = month[flower[2]] + int(flower[3])
    flowers.append([start, end])
flowers.sort()

end_day = 60
cnt = 0
tmp = 0

for flower in flowers:
    if flower[0] > end_day:
        if tmp and flower[0] - tmp <= 0:
            cnt += 1
            end_day = tmp
            tmp = 0
            if end_day > 334:
                break
        else:
            cnt = 0
            break
    tmp = max(tmp, flower[1])
else:
    if tmp:
        cnt += 1
        if tmp <= 334:
            cnt = 0

print(cnt)