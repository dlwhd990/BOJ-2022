# 유기농 배추 [Silver 2]
import sys
sys.setrecursionlimit(1000000)
I = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,visited,ground):
    global cnt
    visited[x][y] = cnt
    for p in range(4):
        nx = x+dx[p]
        ny = y+dy[p]
        if -1 < nx < n and -1 < ny < m and ground[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx,ny,visited,ground)




for _ in range(int(I())):
    m,n,k = map(int,I().split())

    ground = [[0]*m for _ in range(n)]

    for _ in range(k):
        by,bx = map(int,I().split())
        ground[bx][by] = 1

    visited = [[0]*m for _ in range(n)]
    cnt = 1

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and visited[i][j] == 0:
                dfs(i,j,visited,ground)
                cnt += 1

    result = 0

    for i in range(n):
        result = max(result,max(visited[i]))

    print(result)