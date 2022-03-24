import sys
input = sys.stdin.readline
cnt = 0
lst = []
dict = {}
max_count = 0
max_cnt_num = []
N = int(input())

for i in range(N):
    a = int(input())
    if a in dict.keys():
        dict[a] += 1
    else:
        dict[a] = 1
    if dict[a] > max_count:
        max_count = dict[a]
        max_cnt_num.clear()
        max_cnt_num.append(a)
    elif dict[a] == max_count:
        max_cnt_num.append(a)
    lst.append(a)
lst.sort()
max_cnt_num.sort()

print(round(sum(lst)/N))
print(lst[N//2])
if len(max_cnt_num) == 1:
    print(max_cnt_num[0])
else:
    print(max_cnt_num[1])
print(lst[-1]-lst[0])