# 토마토 [Gold 5]
import sys
from collections import deque

I = sys.stdin.readline

m,n = map(int,I().split())
board = []
ripeList = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    board.append(list(map(int,I().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            ripeList.append((i,j))

q = deque()
for ripe in ripeList:
    q.append(ripe)

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            q.append((nx,ny))

result = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            result = -1
            break

        result = max(result,board[i][j])

    if result == -1:
        break

if result == -1:
    print(-1)
else:
    print(result-1)