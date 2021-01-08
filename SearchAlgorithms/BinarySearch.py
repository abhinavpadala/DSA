def binarySearch(arr, left, right, x):
    if right >= 1:
        mid = (left + right) //2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return binarySearch(arr, left, mid-1, x)
        else:
            return binarySearch(arr, mid+1, right, x)
    else:
        return -1
            

if __name__ == '__main__':
    arr = [5,6,7,8,9,10,11]
    print(arr)
    x = int(input('Enter search element:'))
    result = binarySearch(arr, 0, len(arr), x)
    if result == -1:
        print("Element not found")
    else:
        print("Element is at index:", result)