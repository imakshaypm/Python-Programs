def nextPer(arr):
    lists = []
    idx = -1
    l = len(arr)
    for i in range(l - 1 , 0, -1):
        if arr[i] > arr[i - 1]:
            idx = i
            break
    if idx == -1:
        print(arr[::-1])
    else:
        prev = idx
        for i in range(idx+1,l):
            if arr[i] > arr[idx-1] and arr[i] <= arr[prev]:
                prev = i
        arr[idx-1], arr[prev] = arr[prev], arr[idx-1] #Swapping elements
        lists.extend(arr[idx:])
        del arr[idx:]
        arr.extend(lists[::-1])
        print(arr)

a = [1, 3, 2]
nextPer(a)