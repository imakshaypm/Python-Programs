def countAandN(strs):
    di = 0
    ch = 0
    ls = [i for i in strs]
    for i in ls:
        if i.isdigit():
            di += 1
        if i.isalpha():
            ch += 1
    if di == ch:
        return True
    else:
        return False

s = "Geekks12345"
print(countAandN(s))