def preorder(root):
    #1. root 처리
    print(root, end=' ')
    #2. 왼쪽 서브트리 처리
    if len(maps[root]) > 0:
        preorder(maps[root][0])
    #3. 오른쪽 서브트리 처리
    if len(maps[root]) > 1:
        preorder(maps[root][1])

def inorder(root):
    if len(maps[root]) > 0:
        inorder(maps[root][0])
    print(root, end=' ')
    if len(maps[root]) > 1:
        inorder(maps[root][1])

def postorder(root):
    if len(maps[root]) > 0:
        postorder(maps[root][0])
    if len(maps[root]) > 1:
        postorder(maps[root][1])
    print(root, end=' ')

N = 13
inStr = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, inStr.split()))
maps = [[] for _ in range(N+1)]

for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    maps[p].append(c)

print(maps)
# preorder(1)
# print()
# inorder(1)
# print()
# postorder(1)