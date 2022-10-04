def largestElement(arr):
    strarr = list(map(str, arr))
    k = []
    l = []
    s = ""
    for i in strarr:
        if len(i) == 1:
            k.append(int(i * 4))
        else:
            k.append(int(i * 2))
    k.sort()
    while len(k) != 0:
        l.extend(set(str(k[-1])))
        k.pop(k.index(k[-1]))
    s = s + "".join(l)
    return s


l = [1, 34, 3, 98, 9, 76, 45, 4]
print(largestElement(l))