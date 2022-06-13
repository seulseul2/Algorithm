__17626 Four Squares__

```python
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    minV = int(1e9)
    j = 1
    while j**2 <= i:
        minV = min(minV, dp[i-j**2])
        j += 1
    dp.append(minV+1)
print(dp[n])
```

- 해당 문제가 브루트포스라고 생각했는데 dp여서 신기했다.
- 2부터(dp설정을 2까지는 미리 만들어놓았으므로) n까지 숫자를 점진적으로 증가시키면서, 각 숫자에 해당하는 최솟값들을 dp로 쌓아나가는 방식을 배웠다.
- 문제의 key point는 결국 __제곱수 = 1개__이기 때문에, 제곱수를 뺀 만큼의 dp값 중에서 가장 작은 값을 불러온 다음에 제곱수 갯수에 해당하는 +1만큼을 더해주면 된다는 점이었다.
- 다양한 알고리즘을 풀어봤지만, 정말 다양한 풀이 방법이 있고 구현 방법을 명확하게 익힌다면 그만큼 코드는 짧아질 수 있겠다고 생각했다.