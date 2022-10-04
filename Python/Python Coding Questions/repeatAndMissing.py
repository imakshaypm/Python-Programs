def repAndMis(arr):
    arr.sort()
    A = -1
    B = -1
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            A = arr[i]      
        if arr[i+1] - arr[i] > 1:
            B = arr[i] + 1
            
    return A, B


a = [3, 1, 2, 5, 4, 1, 7]
a, b = repAndMis(a)
print("Repeating element:", a, "\nMissing element:", b)