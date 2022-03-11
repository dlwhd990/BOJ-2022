# 배달 [Gold 1]
import sys
from collections import deque
I = sys.stdin.readline
n,m = map(int,I().rstrip().split())
k = []
possible = []
for i in range(n):
    k.append(list(I().rstrip()))
distance = [[int(1e9)]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dir = [[[]for _ in range(m)] for _ in range(n)]
targets = []
t = 0
r = 0
cnt = 0
sx = 0
sy = 0
result = []

for i in range(n):
    for j in range(m):
        if k[i][j] == 'C':
            targets.append((i,j))
        if k[i][j] == 'S':
            sx = i
            sy = j
            k[i][j] = '.'

def bfs(x,y,d,check):
    global distance
    global dir
    global r
    global cnt
    q = deque()
    distance[x][y] = 0
    q.append((x,y,d))
    mx = x
    my = y
    while q:
        x,y,z = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if k[nx][ny] == '#':
                continue
            if z == i:
                continue
            else:
                if k[nx][ny] == '.' and i not in dir[nx][ny]:
                    distance[nx][ny] = distance[x][y] + 1
                    dir[nx][ny].append(i)
                    q.append((nx,ny,i))
                elif k[nx][ny] == 'C':
                    if nx == mx and ny == my:
                        distance[nx][ny] = distance[x][y] + 1
                        dir[nx][ny].append(i)
                        q.append((nx,ny,i))
                    elif check == 1:
                        result.append((nx,ny,distance[x][y]+1,i))
                    else:
                        possible.append((nx,ny,distance[x][y]+1,i))


bfs(sx,sy,-1,0)
ans = int(1e9)
for i in possible:
    distance = [[int(1e9)] * m for _ in range(n)]
    dir = [[[] for _ in range(m)] for _ in range(n)]
    result = []
    bfs(i[0],i[1],i[3],1)
    result.sort(key=lambda x:x[2])

    if result:
        ans = min(ans,result[0][2] + i[2])


if ans == int(1e9):
    print(-1)
else:
    print(ans)