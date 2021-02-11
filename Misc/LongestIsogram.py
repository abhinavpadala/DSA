#Program to print longest isogram

def isoGram(arr):
    temp = ""
    for word in arr:
        if len(set(word)) == len(word) and len(word) > len(temp):
            temp = word
    return temp

arr = ["apple", "abcd", "abcdef", "abb"]
print(isoGram(arr))