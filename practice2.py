def BFS(G, v): #그래프 G, 탐색 시작점 v
    visited = [0]*(n+1) # n은 정점의 갯수
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            visit(t) # 정점 t에서 할 일
        for i in G[t]: # t와 연결된 모든 정점에 대해
            if not visited[i]:
                queue.append(i)