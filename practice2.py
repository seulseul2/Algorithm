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

end_day = 59
cnt = 0
maxV = 0
flag = 1
# 시작점 = 60보다 작은 애중에 제일 큰애
# 그 다음 => 제일 큰애+1 보다 작은애중에 제일 큰애
tmp = []


for flower in flowers:
    if flower[0] <= end_day+1:
        tmp.append(flower[1])
    else:
        if tmp:
            cnt += 1
            end_day = max(tmp)
            if end_day >= 334:
                tmp = []
                break
            tmp = []
            if flower[1] > end_day:
                tmp.append(flower[1])
        else:
            cnt = 0
            flag = 0
            break
if tmp:
    if max(tmp) >= 334:
        cnt += 1
    else:
        cnt = 0
print(cnt)