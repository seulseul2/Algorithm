arr = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21] ,[8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]

I = len(arr)
J = len(arr[0])

mindata = 100000
for i in range(I):
    for j in range(J):
        if arr[i][j] < mindata:
            mindata = arr[i][j]
print(mindata)    