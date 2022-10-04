def reverseArray(arr):
    rarr = []
    print(len(arr))
    for i in range(len(arr) - 1, -1, -1):
        rarr.append(arr[i])
    return rarr

a = [1, 5, 17, 9, 6, 4, -3]
print(reverseArray(a))