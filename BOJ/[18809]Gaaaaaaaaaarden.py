#https://www.acmicpc.net/problem/18809
#Gaaaaaaaaaarden [Gold 1]

import sys
from itertools import combinations as com
from collections import deque
I = sys.stdin.readline

def simulation(n,m,ground,red,green):
    q = deque()
    result = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for x,y in red:
        q.append((0,x,y,8))

    for x,y in green:
        q.append((0,x,y,9))

    while q:
        cnt,x,y,kind = q.popleft()

        if ground[x][y] == "F":
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if ground[nx][ny] == 0 or ground[nx][ny] == "F":
                continue

            if ground[nx][ny] == 1 or ground[nx][ny] == 2:
                ground[nx][ny] = (cnt+1,kind)
                q.append((cnt+1,nx,ny,kind))


            if ground[nx][ny][0] == cnt+1 and abs(ground[nx][ny][1]-kind) == 1:
                ground[nx][ny] = "F"
                result += 1

    return result

def main():
    n, m, g, r = map(int, I().split())
    ground = []
    possible = []
    result = 0
    for _ in range(n):
        ground.append(list(map(int, I().split())))

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 2:
                possible.append((i, j))

    green = list(com(possible, g))
    red = list(com(possible, r))

    for i in range(len(green)):
        tmp = [[0] * m for _ in range(n)]
        for t in range(n):
            for k in range(m):
                tmp[t][k] = ground[t][k]

        for gx, gy in green[i]:
            tmp[gx][gy] = (0,8)

        for j in range(len(red)):
            check = 0
            groundCopy = [[0] * m for _ in range(n)]

            for t in range(n):
                for k in range(m):
                    groundCopy[t][k] = tmp[t][k]

            for rx, ry in red[j]:
                if groundCopy[rx][ry] != 2:
                    check = 1
                    break
                groundCopy[rx][ry] = (0,9)

            if check == 1:
                continue

            result = max(result,simulation(n,m,groundCopy,red[j],green[i]))

    return result

print(main())