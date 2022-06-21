import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tmp = list(map(int, input().split()))
dict = {}
for i in tmp[1:]:
    dict[i] = 1

parties = []

for i in range(M):
    party = list(map(int, input().split()))
    for person in party[1:]:
        if person in dict.keys():
            for tmp in party[1:]:
                if tmp not in dict.keys():
                    dict[tmp] = 1
            break
    else:
        parties.append(party)

while 1:
    flag = 1
    for party in parties:
        for person in party[1:]:
            if person in dict.keys():
                for tmp in party[1:]:
                    if tmp not in dict.keys():
                        dict[tmp] = 1
                parties.remove(party)
                flag = 0
                break
    if flag:
        break

print(len(parties))