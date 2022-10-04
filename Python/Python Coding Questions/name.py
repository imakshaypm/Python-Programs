def solve(s):
    lists = s.split(" ")
    strs = ""
    print(lists)
    for i in range(len(lists)):
        if lists[i] != '':
            strs = lists[i]
        if strs[0].isalpha() and 97 <= ord(strs[0]) <= 122:
            fi = chr(ord(strs[0]) - 32)
            li = list(strs)
            li[0] = fi
            strs = "".join(li)
            lists[i] = strs
        if lists[i] == '':
            lists[i] = ' '
    s = " ".join(lists)
    
    return s
    

s = "132 456 Wq  m e"
print(solve(s))