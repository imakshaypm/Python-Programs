def new_func():
    n = 5
    p = 1
    for i in range(n):
        for j in range(i, n):
            print(p, end=" ")
        p += 1
        print()

new_func()