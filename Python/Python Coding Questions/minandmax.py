def minAndMax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if max < arr[j]:
                max = arr[j]
            if min > arr[j]:
                min = arr[j]
    return min, max

a = [1, 5, 17, 9, 6, 4, -3]
print(minAndMax(a))