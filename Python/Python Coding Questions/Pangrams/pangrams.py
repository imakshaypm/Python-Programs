def accept(strs):
    ls = []
    str1 = strs.lower()
    for i in str1:
        if i.isalpha():
            ls.append(ord(i))
    se = set(ls)
    if len(se) == 26:
        return "Panagram"
    else:
        return "Not Panagram"


s = 'The quick brown fox jumps over the dog'
print(accept(s))