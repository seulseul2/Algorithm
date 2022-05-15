import sys
input = sys.stdin.readline

lst = []
dict = {}

N = int(input())
for i in range(N):
    lst.append(input().rstrip())

for word in lst:
    for j in range(len(word)):
        if word[j] in dict:
            dict[word[j]] += 10**(len(word)-j-1)
        else:
            dict[word[j]] = 10**(len(word)-j-1)

tmp = []
for k in dict.values():
    tmp.append(k)

tmp.sort(reverse=True)
num = 9
ans = 0
for l in tmp:
    ans += num * l
    num -= 1
print(ans)