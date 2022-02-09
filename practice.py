data = [0, 4, 1, 3, 1, 2, 4, 1]
N = max(data)+1

counts = [0] * N

for n in data:
    counts[n] += 1 # [1, 3, 1, 1, 2]

for i in range(1, N):
    counts[i] += counts[i-1] # [1, 4, 5, 6, 8]

result = [-1] * len(data) # [-1, -1, -1, -1, -1, -1, -1, -1]
for i in range(len(data)-1, -1, -1):
    counts[data[i]] -= 1
    result[counts[data[i]]] = data[i]

print(result)