number = int(input("Enter the number: "))


n = number % 8
if n == 0:
    print(2)
if n < 5:
    print(n)
else:
    print(10 - n)

