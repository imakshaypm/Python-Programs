import random


def countingSort(arr):
    # Write your code here
    
    element = max(arr) + 1
    ar = []

    print(arr)
    
    for i in range(element):
        ar.append(0)
    print(ar)
    for j in range(len(ar) - 1):
        ar[arr[j]] += 1
    return ar

a = []
for i in range(100):
    a.append(random.randint(0, 100))

print(countingSort(a))

