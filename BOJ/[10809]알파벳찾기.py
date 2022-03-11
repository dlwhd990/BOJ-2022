# 알파벳 찾기 [Bronze 2]
s = input()
result = [-1]*26

for i in range(len(s)):
    if (result[ord(s[i])-97]) == -1:
        result[ord(s[i])-97] = i

print(*result)