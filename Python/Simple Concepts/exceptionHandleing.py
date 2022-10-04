def div(x, y):
    s = 0
    try:
        s = x / y
    except:
        print("ZeroDivisionError")
    finally:
        print(s)

div(4, 0)