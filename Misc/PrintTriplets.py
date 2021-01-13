# Python program to find three numbers 
# such that sum of two makes the 
# third element in array 
def printTriplet(arr, n):
    #Initially, sort the array
    arr.sort()
    count = 0
    # Fix i in greatest element of the three.
    i = n - 1
    while i >= 0:
        # Traverse from the front and the end to find the 
        # sum that is equal to the greatest element
        j, k = 0, i-1
        while j < k:
            if arr[i] == arr[j] + arr[k]:
                print('Triplets are:', arr[j], arr[k], arr[i])
                j += 1
            elif arr[i] > arr[j] + arr[k]:
                j += 1
            else:
                k -= 1
        i -= 1

arr = [5, 3, 8, 15, 32, 11 ]
#arr = [5, 32, 1, 7, 10, 50, 19, 21, 2]
n = len(arr)
printTriplet(arr, n)