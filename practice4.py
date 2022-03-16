import sys
sys.stdin = open('input (7).txt')

def inorder(root):
    global result
    if len(maps[root]) > 0:
        inorder(maps[root][0])
    result += dict[root]
    if len(maps[root]) > 1:
        inorder(maps[root][1])
    return result

for TC in range(1, 11):
    n = int(input())
    maps = [[] for _ in range(n+1)]
    dict = {}
    result = ''
    for i in range(n):
        lst = list(input().split())
        dict[int(lst[0])] = lst[1]
        if len(lst) > 2:
            for j in range(2, len(lst)):
                maps[i+1].append(int(lst[j]))
    print('#{} {}' .format(TC, inorder(1)))