__1260 DFS와 BFS__

```python
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


# 핵심 : arr[index]별로 숫자 오름차순이 되어있지 않은 경우 순서가 바뀔 수 있기 때문에 가지런하게 만들어준다.
for j in range(1, N+1):
    arr[j].sort()

def dfs(s):
    stack = [s]
    visited = [False] * (N+1)
    lst = []
    while stack:
        start = stack.pop()
        if not visited[start]:
            visited[start] = True
            lst.append(start)
            # 내림차순으로 STACK되도록 설정하여 앞 번호가 우선 검색되도록 만들었다.
            for e in arr[start][::-1]:
                if not visited[e]:
                    stack.append(e)
    return lst

def bfs(s):
    queue = [s]
    visited = [False] * (N+1)
    result = []
    while queue:
        start = queue.pop(0)
        if not visited[start]:
            visited[start] = True
            result.append(start)
            for e in arr[start]:
                if not visited[e]:
                    queue.append(e)
    return result

print(*dfs(V))
print(*bfs(V))
```

- BFS와 DFS 문제는 이해하기가 너무 어려워서 상당히 여러번 복습했고, 여러 문제를 통해 체화하고자 한다.
- 특히 BFS와 DFS 기본 문제를 푸는 데도 많은 손코딩이 필요했고, 이를 머릿속으로 구현하기에는 아직 무리가 있다.
- 그래도 좋았던 점은 디버깅을 하기보다는 눈버깅(눈으로 디버깅)과 손코딩을 하면서 대략 어떤 방식으로 동작하는지를 어렴풋이 이해할 수 있었다.
- 당분간은 BFS+DFS와 백트래킹 문제를 풀어보면서 내 지식으로 만드는 데 집중해야겠다.