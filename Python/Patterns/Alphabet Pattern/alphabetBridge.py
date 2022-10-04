n = 5
p = 65
for i in range(n):
    k = p
    for j in range(i, n):
        print(chr(k), end=" ")
        p += 1
    k -= 1
    print()