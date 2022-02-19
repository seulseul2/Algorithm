# def subSum():
#     for i in range(1, 1<<N): # 각 i는 한개의 부분집합
#         sumV = 0
#         for j in range(N): # i 부분집합의 j번째 비트를 확인
#             if i & (1<<j): # 부분집합에 포함되는 경우
#                 sumV += arr[j]
        
#         if sumV == 0:
#             return True
#     return False

# arr = list(map(int, input().split()))
# print(subSum())


# 단순하게 함수에서 찾는 경우.
def seqSearch(key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [4, 9, 11, 23, 2, 19, 7]

# 새로운거또..
def seqSearch2(key):
    i = 0
    while i < N and arr[i] <= key:
        if arr[i] == key:
            return i
        i += 1
    return -1