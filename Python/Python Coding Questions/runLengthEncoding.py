from collections import Counter

def lenEncoding(string):
    li = []
    di = Counter(string)
    for i in di:
        li.append(i + str(di[i]))
    print("".join(li))

st = "wwwwaaadexxxxxx"

lenEncoding(st)