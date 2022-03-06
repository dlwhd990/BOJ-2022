# 미로 탐색 [Silver 1]
import sys
from collections import deque
I = sys.stdin.readline

n,m = map(int,I().split())
board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    board.append(list(map(int,I().rstrip())))

distance = [[0]*m for _ in range(n)]
distance[0][0] = 1
q = deque()
q.append((0,0))

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue

        if board[nx][ny] == 1 and distance[nx][ny] == 0:
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx,ny))

print(distance[-1][-1])