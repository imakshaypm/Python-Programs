def dupli(arr):
    flag = False
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                flag = True
    return flag

a = [1, 5, 7, 9, 6, 4, 3]
print(dupli(a))