A, B = map(int, input().split())
cnt = 1
while B > A:
    if str(B)[-1] == '1':
        B = int(str(B)[:-1])
        cnt += 1
        continue
    elif B % 2 == 0:
        B //= 2
    else:
        cnt = -1
        break
    cnt += 1

if A != B:
    cnt = -1
    
print(cnt)