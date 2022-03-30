def partitionH(s, e):
    p = s
    lp = s+1
    rp = e
    while lp<=rp:
        while lp<=e and lst[p] >= lst[lp]:
            lp += 1
        while rp>=s and lst[p] < lst[rp]:
            rp -= 1
        if lp<rp: # 넘어갈 수 있기 때문에 무조건 교환하면 안됨.
            lst[lp], lst[rp] = lst[rp], lst[lp]
    lst[rp], lst[p] = lst[p], lst[rp]
    return rp

def partitionL(s, e):
    p = e
    i = -1
    for j in range(e-1):
        if lst[p] > lst[j]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    i += 1
    lst[p], lst[i] = lst[i], lst[p]
    return i


def quickSort(s, e):
    if s<e:
        pivot = partitionL(s, e)
        quickSort(s, pivot-1)
        quickSort(pivot+1, e)

lst = [12, 69, 10, 30, 2, 16, 8, 31, 22]
quickSort(0, len(lst)-1)