def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print(arr)
    selectionSort(arr)
    print(arr)