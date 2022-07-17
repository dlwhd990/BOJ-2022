#https://www.acmicpc.net/problem/16946
#벽 부수고 이동하기 4 [Gold 2]
import sys
from collections import deque
I = sys.stdin.readline

n,m = map(int,I().split())
a = []
countList = []
result = [['0']*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    a.append(list(I().rstrip()))

for i in range(n):
    for j in range(m):
        result[i][j] = a[i][j]

def bfs(sx,sy,graph,districtNum,countList):
    q = deque()
    q.append((sx,sy))

    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if graph[nx][ny] == '0':
                graph[nx][ny] = districtNum
                q.append((nx,ny))
                cnt += 1

    countList.append(cnt)

districtNum = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == '0':
            a[i][j] = districtNum
            bfs(i,j,a,districtNum,countList)
            districtNum += 1


for i in range(n):
    for j in range(m):
        if a[i][j] == '1':
            cnt = 1
            v = []
            for p in range(4):
                nx = i+dx[p]
                ny = j+dy[p]

                if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                    continue

                if a[nx][ny] == '1':
                    continue

                v.append(a[nx][ny])

            for p in list(set(v)):
                cnt += countList[p]

            result[i][j] = str(cnt%10)


for i in result:
    print(''.join(i))