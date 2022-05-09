n = int(input())

lst = [1] * 10
lst[0] = 0
cnt = 1

while n > cnt:
    dp = [0] * 10
    for i in range(10):
        if i != 0:
            dp[i-1] = (dp[i-1] + lst[i]) % 1000000000
        if i != 9:
            dp[i+1] = (dp[i+1] + lst[i]) % 1000000000
    lst = dp
    cnt += 1
print(sum(lst) % 1000000000)