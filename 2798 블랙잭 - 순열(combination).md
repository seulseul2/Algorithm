__순열__

```python
from itertools import combination

n, m = map(int, input().split())
lst = list(map(int, input().split()))
bbob = list(combination(lst, 3)) # combination(찾을 곳, 몇개)
max_num = 0

for i in bbob:
    if max < sum(i) and sum(i) <= m:
        max = sum(i)
print(max)
```

