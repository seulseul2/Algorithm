N = int(input())

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

lst = []
for j in range(N+1):
    if isPrime(j):
        lst.append(j)

cnt = 0
left = 0
right = 1
while right<=len(lst) and left<=right:
    sumV = sum(lst[left:right])
    if sumV < N:
        right += 1
    elif sumV == N:
        cnt += 1
        right += 1
    else:
        left += 1
print(cnt)