def permutation(arr, r): # r => 선택할 요소의 갯수
    arr = sorted(arr) # 의미는 없고, 출력을 예쁘게 하기 위해서 그냥 쓰는거
    used = [0 for _ in range(len(arr))] # 리스트 초기화

    def generate(chosen, used):
        if len(chosen) == r: # 요소를 모두 선택했다면 출력
            n_lst.append([chosen])
            return n_lst
	
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

perm_lst = []
n_lst = []
lst = [3, 2, 1, 5, 4, 6]
permutation(lst, 3)
print(n_lst)

# T = int(input())
# for TC in range(1, T+1):
#     n = int(input())
#     area = [list(map(int, input().split())) for _ in range(n)]
#     arr = [x for x in range(1, n)]
#     perm_lst = []
#     print(perm_lst)