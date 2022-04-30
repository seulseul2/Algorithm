import heapq
import sys
input = sys.stdin.readline

def sync(x):
    while x and not visited[x[0][1]]:
        heapq.heappop(x)

T = int(input())
for TC in range(T):
    k = int(input())
    minheap = []
    maxheap = []
    visited = [False] * 1000001

    for i in range(k):
        char, fake_num = input().rstrip().split()
        num = int(fake_num)
    
        if char == 'I':
            heapq.heappush(minheap, [num, i])
            heapq.heappush(maxheap, [num * -1, i])
            visited[i] = True
    
        elif num == 1:
            sync(maxheap)
            if maxheap:
                visited[maxheap[0][1]] = False
                heapq.heappop(maxheap)
        else:
            sync(minheap)
            if minheap:
                visited[minheap[0][1]] = False
                heapq.heappop(minheap)
    sync(maxheap)
    sync(minheap)
    
    if minheap and maxheap:
        print(-maxheap[0][0], minheap[0][0])
    else:
        print('EMPTY')
