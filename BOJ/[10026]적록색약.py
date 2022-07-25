#https://www.acmicpc.net/problem/10026
#적록색약 [Gold 5]

import sys
sys.setrecursionlimit(10000)
I = sys.stdin.readline
a = []
n = int(I())
for _ in range(n):
    a.append(list(I().rstrip()))

visited = [[0]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global cnt
    visited[x][y] = cnt
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
            continue

        if a[x][y] == a[nx][ny] and visited[nx][ny] == 0:
            dfs(nx,ny)

cnt = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1

print(cnt-1,end=' ')
cnt = 1

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 'R':
            a[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1


print(cnt-1)