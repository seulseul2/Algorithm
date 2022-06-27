import sys
input = sys.stdin.readline
  
def findans(x):
    idx = len(x)-1
    while idx > 0 and x[idx-1] >= x[idx]:
        idx -= 1
    if idx == 0:
        return False
    first = idx - 1

    idx = len(x)-1
    while idx >= 0 and x[idx] <= x[first]:
        idx -= 1
    second = idx

    x[first], x[second] = x[second], x[first]
    result = x[:first+1]
    result.extend(list(reversed(x[first+1:])))
    return result
 
T = int(input())
for TC in range(T):
    word = list(input().rstrip())
    ans = findans(word)
    if not ans:
        print("".join(word))
    else:
        print("".join(ans))