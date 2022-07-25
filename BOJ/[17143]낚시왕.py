#https://www.acmicpc.net/problem/17143
#낚시왕 [Gold 2]

import sys
I = sys.stdin.readline

n,m,s = map(int,I().split())
water = [[[0,0,0,0]for _ in range(m)]for _ in range(n)]
result = 0

for i in range(s):
    tmp = list(map(int,I().split()))
    water[tmp[0]-1][tmp[1]-1] = tmp[2:]+[i]


def moveShark():
    tmp = []
    visited = [0]*s
    for j in range(n):
        for i in range(m):
            if water[j][i][2] == 0:
                continue

            if visited[water[j][i][3]] == 1:
                continue

            x = j
            y = i
            haveToMove = water[j][i][0]
            while haveToMove > 0:
                if water[j][i][1] == 1:
                    if x >= haveToMove:
                        x -= haveToMove
                        break

                    else:
                        haveToMove -= x
                        x = 0
                        water[j][i][1] = 2

                elif water[j][i][1] == 2:
                    if x+haveToMove <= n-1:
                        x += haveToMove
                        break

                    else:
                        haveToMove -= (n-1-x)
                        x = n-1
                        water[j][i][1] = 1

                elif water[j][i][1] == 4:
                    if y >= haveToMove:
                        y -= haveToMove
                        break

                    else:
                        haveToMove -= y
                        y = 0
                        water[j][i][1] = 3

                elif water[j][i][1] == 3:
                    if y + haveToMove <= m - 1:
                        y += haveToMove
                        break

                    else:
                        haveToMove -= (m - 1 - y)
                        y = m - 1
                        water[j][i][1] = 4


            visited[water[j][i][3]] = 1

            tmp.append((x,y,water[j][i][0],water[j][i][1],water[j][i][2],water[j][i][3]))
            water[j][i][0] = 0
            water[j][i][1] = 0
            water[j][i][2] = 0
            water[j][i][3] = 0

    for x,y,a,b,c,d in tmp:
        if water[x][y][2] <= c:
            water[x][y][0] = a
            water[x][y][1] = b
            water[x][y][2] = c
            water[x][y][3] = d






for i in range(m):
    for j in range(n):
        if water[j][i][2] != 0:
            # print("[BEFORE]",i)
            # for p in water:
            #     print(*p)
            # print(result)
            # print("-------------")
            result += water[j][i][2]
            water[j][i][0] = 0
            water[j][i][1] = 0
            water[j][i][2] = 0
            break

    moveShark()
    # print("[AFTER]", i)
    # for p in water:
    #     print(*p)
    # print(result)
    # print("-------------")

print(result)