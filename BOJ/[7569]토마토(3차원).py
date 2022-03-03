# 토마토 [Gold 5]

import sys
from collections import deque

I = sys.stdin.readline

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m,n,h = map(int,I().split())

board = [[]for _ in range(h)]
ripeList = []

for height in range(h):
    for vertical in range(n):
        board[height].append(list(map(int,I().split())))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                ripeList.append((i,j,k))

q = deque()
for ripe in ripeList:
    q.append(ripe)


while q:
    z,x,y = q.popleft()
    for i in range(6):
        nz = z+dz[i]
        nx = x+dx[i]
        ny = y+dy[i]
        if -1 < nz < h and -1 < nx < n and -1 < ny < m and board[nz][nx][ny] == 0:

            board[nz][nx][ny] = board[z][x][y] + 1
            q.append((nz,nx,ny))

result = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                result = -1
                break

            result = max(result,board[i][j][k])

        if result == -1:
            break

    if result == -1:
        break


if result == -1:
    print(result)

else:
    print(result-1)