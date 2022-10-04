from os import popen


def encrpt(secretCode, firstKey, secondKey):
    s = secretCode
    n = firstKey
    m = secondKey
    con = 1000000007
    ans = 0
    r = 1
    f = 1

    for i in range(n % 10):
        r = ((r % 10) * (s % 10)) % 10
        

    for j in range(m % con):
        f = ((f % con)* (r % con)) % con
    ans = f % con

    print(ans)


encrpt(3, 5, 4)