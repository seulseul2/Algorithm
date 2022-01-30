word = input()
c_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c_lst:
    word = word.replace(i, '*')
print(len(word))