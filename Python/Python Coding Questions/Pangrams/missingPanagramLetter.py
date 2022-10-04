def missingPanagram(strs):
    str1 = strs.lower()
    ls = []
    for i in str1:
        if i.isalpha():
            ls.append(ord(i))
    st = set(ls)
    list1 = [i for i in range(98, 123) if i not in st]
    list2 = [chr(i) for i in list1]
    return list2

s = 'The quick brown fox jumps over the dog'
print(missingPanagram(s))