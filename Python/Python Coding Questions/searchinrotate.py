def search(arr, tar):
    index = -1
    mid = len(arr)//2
    arr1 = []
    for i in arr[mid+1:]:
        arr1.append(i)
    for i in arr[0:mid+1]:
        arr1.append(i)
    for i in arr1:
        if i == tar:
            index = arr1.index(i)
    return index
    
    
a = [4, 5, 6, 7, 0, 1, 2]
print(search(a, 7))