from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for TC in range(T):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))

    if n == 0:
        arr = deque()

    R = 0
    for char in p:
        if char == 'R':
            R += 1
        else:
            if not arr:
                print('error')
                break
            if R%2:
                arr.pop()
            else:
                arr.popleft()
    else:
        if R%2:
            arr.reverse()
        print('['+','.join(arr)+']')