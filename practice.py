def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print(x*y//gcd(x, y))