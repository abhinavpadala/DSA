def linearSearch(arr, searchElement):
    n = len(arr)
    for i in range(n):
        if arr[i] == searchElement:
            return i
    return -1


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print(arr)
    searchElement = input("Enter Search Element:")
    result = linearSearch(arr, int(searchElement))
    print(result)
    if result == -1:
        print("Element not found")
    else:
        print("Element is at index:", result)
