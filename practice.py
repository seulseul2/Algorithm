import sys

while 1:
    try:
        x1 = list(map(int, sys.stdin.readline().split()))
        x2 = x1.sort()
        if x2[0]**2 + x2[1]**2 == x2[2]**2:
            print('right')
        else:
            print('wrong')
    except:
        break