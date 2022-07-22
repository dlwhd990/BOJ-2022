#https://www.acmicpc.net/problem/1987
#알파벳 [Gold 4]

import sys
# sys.setrecursionlimit(10000)
I = sys.stdin.readline

a = []
n,m = map(int,I().split())
for _ in range(n):
    a.append(list(I().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]
cnt = 0
result = 0

def dfs(x,y):
    global result,cnt
    visited[x][y] = 1
    checkList[ord(a[x][y])-65] = 1
    cnt += 1
    result = max(result,cnt)

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue

        if checkList[ord(a[nx][ny])-65] == 0:
            dfs(nx,ny)

    cnt -= 1
    checkList[ord(a[x][y])-65] = 0
    return



checkList = [0]*26

dfs(0,0)
print(result)