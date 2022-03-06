# 벽 부수고 이동하기 [Gold 4]
import sys
from collections import deque
I = sys.stdin.readline

n,m = map(int,I().split())
board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    board.append(list(map(int,I().rstrip())))

distance = [[[int(1e10)]*m for _ in range(n)]for _ in range(2)]

q = deque()
q.append((0,0,0))
distance[0][0][0] = 1
while q:
    x,y,count = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue

        if board[nx][ny] == 0 and distance[count][nx][ny] == int(1e10):
            distance[count][nx][ny] = distance[count][x][y] + 1
            q.append((nx,ny,count))

        if count == 0 and board[nx][ny] == 1 and distance[1][nx][ny] == int(1e10):
            distance[1][nx][ny] = distance[0][x][y] + 1
            q.append((nx,ny,1))


if distance[0][-1][-1] == int(1e10) and distance[1][-1][-1] == int(1e10):
    print(-1)

else:
    print(min(distance[0][-1][-1],distance[1][-1][-1]))