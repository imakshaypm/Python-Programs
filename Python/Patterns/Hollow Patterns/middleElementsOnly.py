n = 5 
for i in range(n):
    for j in range(n):
        if n // 2 == i or n // 2 == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()