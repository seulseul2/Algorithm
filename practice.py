T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    queue = []
    num = 0
    cnt = 0

    # 화덕에 피자 넣기
    for i in range(N):
        num += 1
        queue.append([num, cheese[num-1]])

    # 계속해서 돌려주기, 반복
    while 1:
        queue[0][1] = (queue[0][1] // 2)
        if queue[0][1] == 0:
            cnt += 1
            if cnt == M:
                result = queue[0][0]
                break
            num += 1
            if num <= M:
                queue[0][0] = num
                queue[0][1] = cheese[num-1]
            else:
                queue.pop(0)
                continue
        queue.append(queue.pop(0))

    print('#{} {}' .format(TC, result))