import sys
from collections import deque
I = sys.stdin.readline

n,m = map(int,I().split())
a = []
result = 0
time = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    a.append(list(map(int,I().split())))

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            result += 1

while True:
    time += 1
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    target = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if a[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))

            elif a[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                target.append((nx,ny))


    for x,y in target:
        a[x][y] = 0

    if result-len(target) == 0:
        break
    result -= len(target)

print(time)
print(result)