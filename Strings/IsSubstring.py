# Geekforgeeks String problem
# Check if s2 is sub of s1 and
# return index

def isSubString(s1, s2):
    n = len(s1)
    m = len(s2)
    for i in range(n-m+1):
        for j in range(m):
            if s1[i+j] != s2[j]:
                break
        if j + 1 == m:
            return i
    else:
        return -1

s1 = "helloworld"
s2 = "wo"
ans = isSubString(s1, s2)
print(ans)