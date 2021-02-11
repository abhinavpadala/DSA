arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
i, j = 0, len(arr) - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
print(arr)