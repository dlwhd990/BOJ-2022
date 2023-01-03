#https://www.acmicpc.net/problem/15683
#감시 [Gold 4]

# import sys
# from itertools import product as pro
# I = sys.stdin.readline
#
# def search(x,y,n,m,cam,ground):
#     up = []
#     down = []
#     right = []
#     left = []
#     result = [[]for _ in range(4)]
#
#     for i in range(x,-1,-1):
#         if ground[i][y] == 6:
#             break
#         up.append((i,y))
#
#     for i in range(x,n):
#         if ground[i][y] == 6:
#             break
#         down.append((i,y))
#
#     for i in range(y,m):
#         if ground[x][i] == 6:
#             break
#
#         right.append((x,i))
#
#     for i in range(y,-1,-1):
#         if ground[x][i] == 6:
#             break
#         left.append((x,i))
#
#     if cam == 1:
#         result[0].extend(up)
#         result[1].extend(right)
#         result[2].extend(down)
#         result[3].extend(left)
#
#     elif cam == 2:
#         result[0].extend(up)
#         result[0].extend(down)
#         result[2].extend(up)
#         result[2].extend(down)
#         result[1].extend(left)
#         result[1].extend(right)
#         result[3].extend(left)
#         result[3].extend(right)
#
#     elif cam == 3:
#         result[0].extend(up)
#         result[0].extend(right)
#         result[1].extend(down)
#         result[1].extend(right)
#         result[2].extend(left)
#         result[2].extend(down)
#         result[3].extend(up)
#         result[3].extend(left)
#
#     elif cam == 4:
#         result[0].extend(up)
#         result[0].extend(left)
#         result[0].extend(right)
#
#         result[1].extend(up)
#         result[1].extend(down)
#         result[1].extend(right)
#
#         result[2].extend(down)
#         result[2].extend(left)
#         result[2].extend(right)
#
#         result[3].extend(up)
#         result[3].extend(left)
#         result[3].extend(down)
#
#     elif cam == 5:
#         for i in range(4):
#             result[i].extend(up)
#             result[i].extend(left)
#             result[i].extend(down)
#             result[i].extend(right)
#
#     return result
#
# n,m = map(int,I().split())
# ground =  []
# cams = []
# cnt = 0
# walls = 0
# for _ in range(n):
#     ground.append(list(map(int,I().split())))
#
# for i in range(n):
#     for j in range(m):
#         if ground[i][j] == 6:
#             walls += 1
#
#         elif ground[i][j] > 0 and ground[i][j] < 6:
#             cams.append(search(i,j,n,m,ground[i][j],ground))
#             cnt += 1
#
# p = [0,1,2,3]
# poss = list(pro(p,repeat=cnt))
# area = n*m
# result = n*m
#
#
# for i in range(len(poss)):
#     tmp = []
#     for j in range(cnt):
#         tmp.extend(cams[j][poss[i][j]])
#
#     result = min(result,area-len(list(set(tmp)))-walls)
#
# print(result)


# 다시 푼 버전
import sys
from itertools import product as pro
I = sys.stdin.readline

n,m = map(int,I().split())
a = []
cnt = 0
camList = []
result = 65

for _ in range(n):
    a.append(list(map(int,I().split())))


for i in range(n):
    for j in range(m):
        if 0 < a[i][j] < 6:
            cnt += 1
            camList.append((i,j))


p = list(pro([0,1,2,3],repeat=cnt))
b = [(-1,0),(0,1),(1,0),(0,-1)]


def checkDirection(camNum,turn):
    if camNum == 1:
        return [turn]

    if camNum == 2:
        if turn%2 == 0:
            return [0,2]
        else:
            return [1,3]

    if camNum == 3:
        if turn == 0:
            return [0,1]

        if turn == 1:
            return [1,2]

        if turn == 2:
            return [2,3]

        if turn == 3:
            return [0,3]

    if camNum == 4:
        if turn == 0:
            return [0,1,2]

        if turn == 1:
            return [0,1,3]

        if turn == 2:
            return [0,2,3]

        if turn == 3:
            return [1,2,3]

    if camNum == 5:
        return [0,1,2,3]


for t in range(len(p)):
    idx = 0
    r = [[0]*m for _ in range(n)]
    tmp = 0

    for x,y in camList:
        r[x][y] = 1
        direction = checkDirection(a[x][y],p[t][idx])

        # 여기에 방향 따라 감시 가능 구역 표시 (격자 끝, 벽 조심)

        for d in direction:
            nx = x
            ny = y
            while True:
                nx += b[d][0]
                ny += b[d][1]

                if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 or a[nx][ny] == 6:
                    break

                r[nx][ny] = 1

        idx += 1


    for i in range(n):
        for j in range(m):
            if r[i][j] == 0 and a[i][j] != 6:
                tmp += 1

    result = min(result,tmp)


print(result)
