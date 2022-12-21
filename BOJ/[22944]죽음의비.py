# 죽음의 비 [Gold 4]

import sys
from itertools import permutations as per
I = sys.stdin.readline

def main():
    n, h, d = map(int, I().split())
    a = []
    s = [0, 0]
    e = [0, 0]
    um = []
    p = []
    result = int(1e10)
    for _ in range(n):
        a.append(list(I().rstrip()))

    for i in range(n):
        for j in range(n):
            if a[i][j] == 'U':
                um.append((i, j))

            elif a[i][j] == 'S':
                s = [i, j]

            elif a[i][j] == 'E':
                e = [i, j]

    if abs(s[0]-e[0])+abs(s[1]-e[1]) <= h:
        return abs(s[0]-e[0])+abs(s[1]-e[1])

    for i in range(1, len(um) + 1):
        p.extend(list(per(um, i)))

    for i in p:
        sx = s[0]
        sy = s[1]
        health = h
        nowUm = 0
        check = 0
        tmp = 0
        for x, y in i:
            dist = abs(sx-x)+abs(sy-y)
            if dist <= health+nowUm:
                if nowUm-dist < 0:
                    health -= (dist-nowUm-1)

                nowUm = d-1
                tmp += dist
                sx = x
                sy = y

            else:
                check = 1
                break

        if check == 0:
            if (abs(sx-e[0])+abs(sy-e[1])) <= health+nowUm:
                result = min(result,tmp+(abs(sx-e[0])+abs(sy-e[1])))

    if result == int(1e10):
        return -1
    return result

print(main())