import sys
input = sys.stdin.readline

def zett(y, x, num):
    global cnt
    if num == 1:
        if y == r and x == c:
            print(cnt)
            return
        else:
            cnt += 1
            return
    if y<=r<y+num//2 and x<=c<x+num//2:
        zett(y, x, num//2)
        return
    elif y<=r<y+num//2 and x+num//2<=c<x+num:
        cnt += (num**2)//4
        zett(y, x+num//2, num//2)
        return
    elif y+num//2<=r<y+num and x<=c<x+num//2:
        cnt += (num**2)//2
        zett(y+num//2, x, num//2)
        return
    elif y+num//2<=r<y+num and x+num//2<=c<x+num:
        cnt += (num**2)//4*3
        zett(y+num//2, x+num//2, num//2)
        return

N, r, c = map(int, input().split())
n = 2**N
cnt = 0
zett(0, 0, n)