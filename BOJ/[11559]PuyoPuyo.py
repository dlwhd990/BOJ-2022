# Puyo Puyo [Gold 4]

import sys
from collections import deque
I = sys.stdin.readline

board = []

for _ in range(12):
    board.append((list(I().rstrip())))

boom = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,target):
    q = deque()
    q.append((x,y))
    distance = [[-1]*6 for _ in range(12)]
    distance[x][y] = 0
    boom = [(x,y)]
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue

            if board[nx][ny] == target and distance[nx][ny] == -1:
                distance[nx][ny] = 1
                q.append((nx,ny))
                boom.append((nx,ny))

    return boom

cnt = 0

while True:
    boom = []
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and visited[i][j] == 0:
                result = bfs(i, j, board[i][j])
                if len(result) > 3:
                    for p in result:
                        boom.append(p)
                        visited[p[0]][p[1]] = 1

    if len(boom) == 0:
        break

    cnt += 1
    for x, y in boom:
        board[x][y] = '.'

    for i in range(6):
        tmp = []
        for j in range(12):
            tmp.append(board[j][i])

        if tmp.count('.') == 12:
            continue

        ttmp = []
        for j in range(12):
            if tmp[j] != '.':
                ttmp.append(tmp[j])

        tmp = ['.']*(12-len(ttmp))
        tmp.extend(ttmp)

        for j in range(12):
            board[j][i] = tmp[j]


print(cnt)