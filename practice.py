from collections import deque
import sys
input = sys.stdin.readline

def bfs(A, B, C):
    q = deque([(len(A), len(B), len(C))])
    visited = [[0]*(len(B)+1) for _ in range(len(A)+1)]
    while q:
        aIndex, bIndex, cIndex = q.popleft()
        if aIndex == bIndex == cIndex == 0:
            return True
        elif cIndex == 0:
            return False
        
        if aIndex > 0 and A[aIndex-1] == C[cIndex-1] and visited[aIndex-1][bIndex] == 0:
            visited[aIndex-1][bIndex] = 1
            q.append([aIndex-1, bIndex, cIndex-1])
        if bIndex > 0 and B[bIndex-1] == C[cIndex-1] and visited[aIndex][bIndex-1] == 0:
            visited[aIndex][bIndex-1] = 1
            q.append([aIndex, bIndex-1, cIndex-1])
    return False

T = int(input())
for TC in range(1, T+1):
    F, S, C = input().rstrip().split()
    if bfs(F, S, C):
        print(f"Data set {TC}: yes")
    else:
        print(f"Data set {TC}: no")