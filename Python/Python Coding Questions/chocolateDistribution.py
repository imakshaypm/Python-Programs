from hashlib import new


def differace(arr, m):
    for j in range(m):
        for k in range(j + 1, len(arr)):
            if arr[j] > arr[k]:
                temp = arr[j]
                arr[j] =arr[k]
                arr[k] = temp
    diff = arr[m - 1] - arr[0]
    return diff, arr
    

a = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
print(differace(a,7))


