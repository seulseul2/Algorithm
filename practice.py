def isPrime(num):
    if num == 1: # 1은 어차피 소수가 아니니까 취급 X
        return False
    else:
        for i in range(2, int(num**0.5) + 1): # num을 나누어줄 range는 2부터 num의 제곱근까지
            if num % i == 0:
                return False
        return True
    
M, N = map(int, input().split())

for i in range(M, N, +1):
    if isPrime(i): # isPrime(i)의 결과가 True라면
        print(i)