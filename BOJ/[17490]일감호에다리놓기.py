# 일감호에 다리 놓기 [Gold 3]

import sys
I = sys.stdin.readline

def main():
    n, m, k = map(int, I().split())
    s = list(map(int, I().split()))
    check = 0
    costs = 0
    t = []

    for _ in range(m):
        x,y = map(int,I().split())
        if min(x,y) == 1 and max(x,y) == n:
            check = 1
        else:
            t.append((min(x,y),max(x,y)))

    if m <= 1:
        return "YES"

    t.sort()

    for i in range(1,len(t)):
        if t[i-1][1]-1 < t[i][0]:
            costs += min(s[t[i-1][1]-1:t[i][0]])

    if check == 1:
        if t[0][0] > 0:
            costs += min(s[:t[0][0]])
        if t[-1][1]-1 < n:
            costs += min(s[t[-1][1]-1:])

    else:
        if t[0][0] > 0 or t[-1][1]-1 < n:
            costs += min(min(s[:t[0][0]]),min(s[t[-1][1]-1:]))

    if costs <= k:
        return "YES"
    return "NO"


print(main())