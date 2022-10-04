n = 4
c = 1
for i in range(n):
    for j in range(i+1):
        print("   ", end=" ")
    for j in range(i, n):
        print(str(c) + " *", end=" ")
        c += 1
    print()
