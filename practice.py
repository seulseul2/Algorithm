import sys
input = sys.stdin.readline
n = int(input())
N = int(input())
word = input().rstrip()
idx = 0
cnt = 0
result = 0

while idx <= N-2:
    if word[idx:idx+3] == 'IOI':
        cnt += 1
        idx += 2
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        cnt = 0
        idx += 1
print(result)