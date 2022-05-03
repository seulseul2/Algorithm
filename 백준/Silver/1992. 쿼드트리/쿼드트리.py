import sys
input = sys.stdin.readline

def four_square(y, x, num):
    global result
    standard = maps[y][x]
    for i in range(y, y+num):
        for j in range(x, x+num):
            if maps[i][j] != standard:
                result = result+'('
                four_square(y, x, num//2)
                four_square(y, x+(num//2), num//2)
                four_square(y+(num//2), x, num//2)
                four_square(y+(num//2), x+(num//2), num//2)
                result = result+')'
                return
    result = result + str(standard)

N = int(input())
maps = [list(map(int, input().rstrip())) for _ in range(N)]
result = ''
four_square(0, 0, N)
print(result)