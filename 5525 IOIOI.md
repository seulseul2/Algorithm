__5525 IOIOI__

__50점짜리 코드__

```python
import sys
input = sys.stdin.readline
n = int(input())
N = int(input())
word = input().rstrip()
p = 'I' + 'OI' * n
x = 2*n+1
cnt = 0

for idx in range(N-n):
    if word[idx:idx+x] == p:
        cnt += 1
print(cnt)
```

- 해당 코드로 정답이 나올 줄 알았는데, 시간초과로 50점이 나왔다.
- 파이파이로 돌려도 50점 시간초과고 if word[idx] == 'I'를 넣어도 50점 시간초과여서(사실 이건 될거라고 생각 안했다) 다른 방법을 찾기로 했다.
- 출제자의 의도를 생각해봤을 때, IOI라는 규칙성이 있기 때문에 for문보다는 while문을 가지고 규칙성을 찾아가면서 IOI 관련 문자열이 나오면 idx에 +2하면서 계속 찾기 / 안나오면 +1 하면서 IOI 나올때까지 찾는 방법이 적합하다고 생각했다.

__맞은 코드__

```python
import sys
input = sys.stdin.readline
n = int(input())
N = int(input())
word = input().rstrip()
idx = 0
cnt = 0
result = 0

while idx <= N-2:
    if word[idx:idx+3] == 'IOI':
        cnt += 1
        idx += 2
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        cnt = 0
        idx += 1
print(result)
```

- idx때문에 범위 문제로 조금 걱정을 했는데 다행히도 맞았다. 문자열 규칙성 관련 문제를 풀 때 많은 참조가 될 것 같은 문제인 듯