n = 10
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    for j in range(i):
        print(" ", end=" ")
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    for j in range(i, n - 1):
        print(" ", end=" ")
    for j in range(i, n - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()