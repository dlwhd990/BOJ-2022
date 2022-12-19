# 일감호에 다리 놓기 [Gold 3]

import sys
I = sys.stdin.readline

def main():
    n, m, k = map(int, I().split())
    s = list(map(int, I().split()))
    mak = []
    costs = 0
    t = []
    check = 0
    for _ in range(m):
        x, y = map(int, I().split())
        if min(x, y) == 1 and max(x, y) == n:
            check = 1
        else:
            mak.append((min(x, y), max(x, y)))


    mak.sort()

    if m <= 1:
        return "YES"

    t.append((1,mak[0][0]))
    for i in range(1,len(mak)):
        t.append((mak[i-1][1],mak[i][0]))

    if check == 0:
        for i in range(len(t)):
            if i == 0:
                costs += min(min(s[t[-1][1]-1:]),min(s[t[i][0]-1:t[i][1]]))
            else:
                costs += min(s[t[i][0]-1:t[i][1]])
    else:
        for i in range(len(t)):
            costs += min(s[t[i][0]-1:t[i][1]])

    if k >= costs:
        return "YES"
    return "NO"

print(main())
