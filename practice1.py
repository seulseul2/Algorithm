import sys
input = sys.stdin.readline

def checkpaper(y, x, n):
    global white
    global blue
    standard = papers[y][x]
    if n != 1:
        for i in range(y, y+n):
            for j in range(x, x+n):
                if papers[i][j] != standard:
                    checkpaper(y, x, n//2)
                    checkpaper(y+n//2, x+n//2, n//2)
                    checkpaper(y+n//2, x, n//2)
                    checkpaper(y, x+n//2, n//2)
                    return
    if standard == 1:
        blue += 1
        return
    else:
        white += 1
        return

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0
checkpaper(0, 0, N)
print(white)
print(blue)