lst = list(map(int, input().split()))

n = len(lst)

for i in range(1<<n): # 0 ~ 1023까지
    for j in range(n): # j는 0~9까지
        if i & (1<<j): # 만약에 0~1023과 1<<j 사이 부분집합이 있다면
            print(lst[j], end=' ') # j를 출력해라~ 뭐 그런뜻인거같은데 시 팔
    print()
print()