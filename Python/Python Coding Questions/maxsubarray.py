def maxSubarray(arr, size):
    sum = 0
    end = 0
    for i in range(size):
        end = end + arr[i]
        if sum < end:
            sum = end
        if end < 0:
            end = 0
    return sum


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubarray(a, len(a)))
