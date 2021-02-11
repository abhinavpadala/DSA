def sortString(s):
    max_char = 26
    sortedString = ""
    char_count = [0] * max_char
    for i in range(len(s)):
        char_count[ord(s[i]) - ord('a')] += 1
    for i in range(max_char):
        for j in range(char_count[i]):
            sortedString = sortedString + chr(ord('a') + i)
    return sortedString
            
if __name__ == "__main__":
    n = int(input())
    ans = []
    for i in range(n):
        s = str(input())
        ans.append(sortString(s))
    for each_ans in ans:
        print(each_ans)
        