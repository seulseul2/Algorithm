N, M = map(int, input().split())
dict = {}
for i in range(N):
    url, password = input().split()
    dict[url] = password
for j in range(M):
    x = input()
    print(dict[x])