__1013 contact__

```python
import re
T = int(input())
for TC in range(T):
    word = input()
    x = re.compile('(100+1+|01)+')
    if x.fullmatch(word):
        print('YES')
    else:
        print('NO')
```

