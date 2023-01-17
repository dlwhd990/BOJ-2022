# 보스몬스터 전리품 [Gold 3]
import sys
from collections import deque
I = sys.stdin.readline

n,m,c = map(int,I().split())
a = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dist = []
damage = dict()
for _ in range(n):
    a.append(list(I().rstrip()))


for _ in range(c):
    x,y = I().rstrip().split()
    damage[x] = int(y)

bossHP = int(I())

q = deque()
people = []
for i in range(n):
    for j in range(m):
        if 97 <= ord(a[i][j]) <= 122:
            people.append((i,j,a[i][j]))
            a[i][j] = '.'

def bfs(x,y,who):
    distance = [[-1]*m for _ in range(n)]
    distance[x][y] = 0
    q.append((x,y,who))
    while q:
        x,y,who = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if a[nx][ny] == '.' and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny,who))

            elif a[nx][ny] == 'B' and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                dist.append((distance[nx][ny],damage[who]))
                break


for x,y,who in people:
    bfs(x,y,who)


t = dict()

result = 0
total = 0
for x,y in dist:
    if x not in t:
        t[x] = [y,1]
    else:
        t[x] = [t[x][0]+y,t[x][1]+1]

i = 0
while True:
    i += 1
    if i in t:
        total += t[i][0]
        result += t[i][1]

    bossHP -= total
    if bossHP <= 0:
        break

print(result)