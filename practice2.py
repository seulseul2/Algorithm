T = int(input())
for TC in range(T):
    n = int(input())
    log = list(map(int, input().split()))
    log.sort()

    minV = 0
    for i in range(2, n):
        if abs(log[i] - log[i-2]) > minV:
            minV = abs(log[i] - log[i-2])
    print(minV)