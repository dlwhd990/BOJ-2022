# 졸려 [Gold 5]
import sys
I = sys.stdin.readline

n = int(I())
s = I().rstrip()
original = s
hubo = [s]

for i in range(len(s)):
    left = ''
    right = ''
    for j in range(len(s)):
        if j%2 == 0:
            left += s[j]
        else:
            right += s[j]

    s = left + right[::-1]

    if s == original:
        break

    else:
        hubo.append(s)

n %= len(hubo)
print(hubo[n])