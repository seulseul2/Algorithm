import sys
input = sys.stdin.readline
N = int(input())
strN = str(N)
M = int(input())
if M:
    broken = list(input().split())
    # 1. 100번에서 +나 -를 눌러서 가는 방법
    minV = abs(N-100)
    if minV <= len(strN) or M == 10:
        print(minV)
    else:
        # 가장 가까운 수를 구한 다음, 더해서 가는 방법
        cnt = 0
        while 1:
            cnt += 1
            intA = N + cnt
            strA = str(intA)
            for number in broken:
                if number in strA:
                    break
            else:
                standard = intA
            intB = N - cnt
            if intB < 0:
                continue
            strB = str(intB)
            for number in broken:
                if number in strB:
                    break
            else:
                if len(strB) < len(strA):
                    standard = intB
            if standard:
                break
        print(min(minV, len(str(standard))+abs(standard-N)))
else:
    print(min(len(strN), abs(N-100)))