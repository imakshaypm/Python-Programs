from multiprocessing.forkserver import read_signed


def accept(strs):
    lst = ['a','e', 'i', 'o', 'u']
    lst1 = ['A', 'E', 'I', 'O', 'U']
    lst2 = []
    lst3 = []
    for i in strs:
        if lst in strs:
            k = lst.index(i)
            lst2.append(lst[k])
            lst.pop(k)
        if lst1 in strs:
            k = lst1.index(i)
            lst3.append(lst1[k])
            lst1.pop(k)
    if len(lst2) + len(lst3) == 5:
        return "Accepted"
    else:
        return "Not Accepted"


s = 'aeiou'
print(accept(s))