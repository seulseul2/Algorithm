__9663 N_queen__

```python
import sys
input = sys.stdin.readline

n = int(input())
y = [0] * n
cnt = 0

def prove(x):
    for i in range(x):
        if y[x] == y[i] or abs(y[x] - y[i]) == abs(x-i):
            return False
    return True

def queen(x):
    global cnt
    if x == n:
        cnt += 1
        return
    else:
        for i in range(n):
            y[x] = i
            if prove(x):
                queen(x+1)
queen(0)
print(cnt)
```

