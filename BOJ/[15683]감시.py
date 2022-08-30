#https://www.acmicpc.net/problem/15683
#감시 [Gold 4]

import sys
from itertools import product as pro
I = sys.stdin.readline

def search(x,y,n,m,cam,ground):
    up = []
    down = []
    right = []
    left = []
    result = [[]for _ in range(4)]

    for i in range(x,-1,-1):
        if ground[i][y] == 6:
            break
        up.append((i,y))

    for i in range(x,n):
        if ground[i][y] == 6:
            break
        down.append((i,y))

    for i in range(y,m):
        if ground[x][i] == 6:
            break

        right.append((x,i))

    for i in range(y,-1,-1):
        if ground[x][i] == 6:
            break
        left.append((x,i))

    if cam == 1:
        result[0].extend(up)
        result[1].extend(right)
        result[2].extend(down)
        result[3].extend(left)

    elif cam == 2:
        result[0].extend(up)
        result[0].extend(down)
        result[2].extend(up)
        result[2].extend(down)
        result[1].extend(left)
        result[1].extend(right)
        result[3].extend(left)
        result[3].extend(right)

    elif cam == 3:
        result[0].extend(up)
        result[0].extend(right)
        result[1].extend(down)
        result[1].extend(right)
        result[2].extend(left)
        result[2].extend(down)
        result[3].extend(up)
        result[3].extend(left)

    elif cam == 4:
        result[0].extend(up)
        result[0].extend(left)
        result[0].extend(right)

        result[1].extend(up)
        result[1].extend(down)
        result[1].extend(right)

        result[2].extend(down)
        result[2].extend(left)
        result[2].extend(right)

        result[3].extend(up)
        result[3].extend(left)
        result[3].extend(down)

    elif cam == 5:
        for i in range(4):
            result[i].extend(up)
            result[i].extend(left)
            result[i].extend(down)
            result[i].extend(right)

    return result

n,m = map(int,I().split())
ground =  []
cams = []
cnt = 0
walls = 0
for _ in range(n):
    ground.append(list(map(int,I().split())))

for i in range(n):
    for j in range(m):
        if ground[i][j] == 6:
            walls += 1

        elif ground[i][j] > 0 and ground[i][j] < 6:
            cams.append(search(i,j,n,m,ground[i][j],ground))
            cnt += 1

p = [0,1,2,3]
poss = list(pro(p,repeat=cnt))
area = n*m
result = n*m


for i in range(len(poss)):
    tmp = []
    for j in range(cnt):
        tmp.extend(cams[j][poss[i][j]])

    result = min(result,area-len(list(set(tmp)))-walls)

print(result)