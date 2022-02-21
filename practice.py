N = int(input())
for i in range(6):
    lst = [] # 방향 리스트
    dict = {} # 거리 리스트
    direction, distance = map(int, input().split())
    if direction not in lst:
        lst.append(direction)
    else:
        if direction == 1:
            if 2 in lst: