# A majority element in an array A of size N is an
# element that appears more than N/2 times in the array.

# Solved using Hashmap
def findMajority(arr, n):
    tDict = {}
    majorityElement = -1
    for i in range(n):
        if arr[i] in tDict:
            tDict[arr[i]] += 1
        else:
            tDict[arr[i]] = 1
    for key in tDict:
        if tDict[key] > n/2:
            majorityElement = key
            break
    return majorityElement


arr = [3, 6, 2, 3, 3, 3, 5, 8, 3]
n = len(arr)
print(findMajority(arr, n))

"""
Time Complexity: O(n). 
One traversal of the array is needed, so the time complexity is linear.
Auxiliary Space: O(n). 
Since a hashmap requires linear space.
"""
