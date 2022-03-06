# チーズ (Cheese) [Gold 5]
import sys
from collections import deque

I = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ground = []
result = 0
n,m,k = map(int,I().split())
for _ in range(n):
    ground.append(list(I().rstrip()))

start = -1

for i in range(n):
    for j in range(m):
        if ground[i][j] == 'S':
            start = (i,j)
            ground[i][j] = '.'
            break

    if start != -1:
        break


def simulation():
    global k
    global result
    global check
    global level
    global start
    q = deque()
    q.append(start)
    distance = [[-1] * m for _ in range(n)]
    distance[start[0]][start[1]] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if ground[nx][ny] == 'X':
                continue

            if ground[nx][ny] == '.' and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

            elif ground[nx][ny].isdigit() and distance[nx][ny] == -1 and int(ground[nx][ny]) > level:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))

            elif ground[nx][ny].isdigit() and distance[nx][ny] == -1 and int(ground[nx][ny]) <= level:
                k += int(ground[nx][ny])
                ground[nx][ny] = '.'
                result += distance[x][y] + 1
                check = 1
                level += 1
                start = (nx,ny)
                return distance

level = 1
while True:
    check = 0
    simulation()
    if check == 0:
        break

print(result)