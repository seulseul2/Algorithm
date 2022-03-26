import sys
input = sys.stdin.readline

def heapIn(value):
    global last
    last += 1
    TREE[last] = value
    c = last
    p = c//2
    while p>=1 and TREE[p] > TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        c = p
        p = c//2

def heapPop():
    global last
    print(TREE[1])
    result = TREE[1]
    TREE[1], TREE[last] = TREE[last], TREE[1]
    TREE[last] = 0
    last -= 1

    p = 1 
    c = p*2
    if c+1 <= last and TREE[c] > TREE[c+1]:
        c += 1
    
    while c<=last and TREE[p] > TREE[c]:
        TREE[p], TREE[c] = TREE[c], TREE[p]
        p = c
        c = p*2
        if c+1 <= last and TREE[c] > TREE[c+1]:
            c += 1

N = int(input())
TREE = [0] * (N+1)
last = 0
for i in range(N):
    x = int(input())
    if x == 0:
        if TREE[1] == 0:
            print(0)
        else:
            heapPop()
    else:
        heapIn(x)