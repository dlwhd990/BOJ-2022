# 빙산 [Gold 4]

import sys
sys.setrecursionlimit(100000)
I = sys.stdin.readline

n,m = map(int,I().split())
board = []
for _ in range(n):
    board.append(list(map(int,I().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue

        if board[nx][ny] != 0 and visited[nx][ny] == 0:
            dfs(nx,ny)

result = 0

while True:
    result += 1
    minus = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                cnt = 0
                for p in range(4):
                    if board[i+dx[p]][j+dy[p]] == 0:
                        cnt += 1

                minus.append((i,j,cnt))

    for a,b,c in minus:
        board[a][b] = max(0,board[a][b]-c)


    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and visited[i][j] == 0:
                dfs(i,j)
                cnt += 1


    if cnt != 1:
        break

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            cnt += 1

if cnt == 0:
    print(0)
else:
    print(result)