def partitionH(s, e):
    p = s
    lp = s+1
    rp = e
    while lp <= rp:
        while lp <= e and lst[s] > lst[lp]:
            lp += 1
        while rp >= s and lst[p] < lst[rp]:
            rp -= 1
        if lp < rp:
            lst[lp], lst[rp] = lst[rp], lst[lp]
    lst[rp], lst[p] = lst[p], lst[rp]
    return rp

# def partitionL(s, e):
#     p = e
#     i = -1
#     for j in range(e):
#         if lst[p] > lst[j]:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#     i += 1
#     lst[p], lst[i] = lst[i], lst[p]
#     return i

def quickSort(s, e):
    if s<e:
        pivot = partitionH(s, e)
        quickSort(s, pivot-1)
        quickSort(pivot+1, e)


lst = [12, 69, 10, 30, 2, 16, 8, 31, 22]
quickSort(0, len(lst)-1)
print(lst)