import sys

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5+1)):
            if num % i == 0:
                return False
        return True

lst = list(range(2, 10001)) # 미리 제한된 범위를 가진 리스트를 생성
sosu = [] # 소수만 저장할 리스트 생성

for i in lst:
    if isPrime(i):
        sosu.append(i) # 범위 내 소수 리스트 생성

n = int(sys.stdin.readline())
jjin = []
for i in range(n):
    x = int(sys.stdin.readline()) # 소수로 나누어줄 짝수 x값을 받아준다.
    for a in sosu:
        if a < x:
            jjin.append(a)
    for b in jjin:
        for c in jjin:
            if b + c == x:
                print(b, c, sep=' ')