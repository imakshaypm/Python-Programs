def repeatingChar(strs):
    dic = {}
    str1 = list(strs.lower())
    for i in str1:
        if i.isalpha():
            dic[i] = str1.count(i)
    value = [i for i in dic if dic[i] == 1]
    print(value[0])

s = 'GeeksQuiz'
repeatingChar(s)