N = int(input())
seat = input()
couple = 0
for i in seat:
    if i == 'L':
        couple += 1
result = (N+1) - couple//2

if N <= result:
    print(N)
else:
    print(result)