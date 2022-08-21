#https://www.acmicpc.net/problem/23562
#ㄷ 만들기 [Gold 5]

import sys
I = sys.stdin.readline

def makeDigut(k):
    digut = [["."]*(k*3) for _ in range(k*3)]

    for i in range(k):
        for j in range(k*3):
            digut[i][j] = "#"

    for i in range(k):
        for j in range(k):
            digut[k+i][j] = "#"

    for i in range(k):
        for j in range(k*3):
            digut[k*2+i][j] = "#"

    return digut


def main():
    ground = []
    result = int(1e10)
    blackCnt = 0
    n,m = map(int,I().split())
    a,b = map(int,I().split())
    for _ in range(n):
        ground.append(list(I().rstrip()))

    for i in range(n):
        for j in range(m):
            if ground[i][j] == "#":
                blackCnt += 1

    short = min(n,m)
    for k in range(1,short//3+1):
        digut = makeDigut(k)

        for i in range(n):
            for j in range(m):
                cnt = 0
                bCnt = 0
                if i+k*3-1 > n-1 or j+k*3-1 > m-1:
                    continue

                for x in range(k*3):
                    for y in range(k*3):
                        if ground[i+x][j+y] == "#":
                            bCnt += 1

                        if digut[x][y] == "." and ground[i+x][j+y] == "#":
                            cnt += b

                        elif digut[x][y] == '#' and ground[i+x][j+y] == ".":
                            cnt += a

                cnt += (blackCnt-bCnt)*b
                result = min(cnt,result)

    return result

print(main())