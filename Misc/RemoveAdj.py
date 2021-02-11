#Recursively remove all adjacent duplicates
def removeAdj(s, low, high):
    while high > 1:
        mid = (low + (high - 1))//2
        while mid > 0:
            if s[mid] == s[mid+1]:
                s.pop(mid)
                s.pop(mid + 1)
            if s[mid] == s[mid-1]:
                s.pop(mid)
                s.pop(mid-1)
            removeAdj(s, low, len(s))

original_string = "geeksforgeeks"
s = list(original_string)
removeAdj(s, 0, len(s))
print(s)