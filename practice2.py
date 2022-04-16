import sys
input = sys.stdin.readline

c_n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
box_n = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)
time = 0
cnt = 0

if crane[0] < box[0]:
    print(-1)
else:
    while cnt < box_n:
        for i in range(c_n):
            if crane[i] >= box[cnt]:
                cnt += 1
                if cnt == box_n:
                    break
                continue
        time += 1
    print(time)