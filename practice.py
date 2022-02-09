a, b = map(int, input().split())
x = list(map(int, input().split()))
result = 0
lst = []

for i in range(len(x)):
    for j in range(i+1, len(x)):
        for k in range(j+1, len(x)):
            result = x[i] + x[j] + x[k]
            if result <= b:
                lst.append(result)
print(max(lst))