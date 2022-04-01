def dfs(idx):
    global charge, result

    if idx >= len(lst): # 끝까지 도달했을 경우
        if result >= charge: # 충전 값이 최소 충전값보다 작다면
            result = charge # 갱신
        return

    if result <= charge: # 끝까지 도달 안했는데도 최소 충전값과 같거나 그보다 크다면
        return # 더 해볼 필요 없음

    for i in range(idx+lst[idx], idx, -1): #뒤에서부터 역으로 탐색
        charge += 1
        dfs(i)
        charge -= 1


T = int(input())

for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    result = 987654321
    charge = 0
    dfs(1)

    print(f'#{test_case} {result-1}')