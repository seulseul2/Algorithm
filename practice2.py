T = int(input())

for TC in range(1, T+1):
    N = int(input())
    result = {}
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            if j in result.keys():
                result[j] += 1
            else:
                result[j] = 1
    P = int(input())

    print('#{}' .format(TC), end=' ')
    for idx in range(1, len(result)+1):
        if idx == P:
            print(result.get(idx))
        else:
            print(result.get(idx), end=' ')