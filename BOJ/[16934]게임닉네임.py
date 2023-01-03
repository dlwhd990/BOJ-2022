#게임 닉네임 [Gold 3]
import sys
I = sys.stdin.readline

n = int(I())
d = dict()
t = dict()
for _ in range(n):
    s = I().rstrip()
    check = 0
    tmp = ''
    for i in s:
        tmp += i
        if check == 0 and tmp not in d:
            check = 1
            print(tmp)

        d[tmp] = 1

    if s in t:
        t[s] += 1

    else:
        t[s] = 1

    if check == 0:
        if t[s] == 1:
            print(s)

        else:
            print(s+str(t[s]))