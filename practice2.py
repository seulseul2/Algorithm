T = int(input())
for TC in range(1, T+1):
    lst = [1, 3]
    N = int(input())
    n = N // 10
    if n < 3:
        result = lst[n-1]
    else:
        for i in range(n-2):
            lst.append(lst[-1]+lst[-2]*2)
        result = lst[-1]
    print('#{} {}' .format(TC, result))