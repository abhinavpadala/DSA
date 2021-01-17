#Merge two strings
#Geekforgeeks String problem
"""
Example:
Input:
2
Hello Bye
abc def

Output:
HBeylelo
adbecf
"""

def mergeStrings(s1, s2):
    s3 = ""
    for i in range(max(len(s1), len(s2))):
        if i < len(s1) and i < len(s2):
            s3 = s3 + s1[i] + s2[i]
        elif i < len(s1):
            s3 = s3 + s1[i]
        elif i < len(s2):
            s3 = s3 + s2[i]
    return s3

if __name__ == "__main__":
  n = int(input())
  ans = []
  for _ in range(n):
    x, y = input().split()
    ans.append(mergeStrings(x, y))
  for each_ans in ans:
    print(each_ans)