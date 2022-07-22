#https://www.acmicpc.net/problem/16234
#인구 이동 [Gold 5]
import sys
from collections import deque
I = sys.stdin.readline

n,l,r = map(int,I().split())
a = []
result = 0
for _ in range(n):
    a.append(list(map(int,I().split())))

def search(graph,visited,sx,sy):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[sx][sy] = 1
    q = deque()
    q.append((sx,sy))
    tmp = [(sx,sy)]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if visited[nx][ny] == 0 and (l <= abs(graph[nx][ny] - graph[x][y]) <= r):
                visited[nx][ny] = 1
                tmp.append((nx,ny))
                q.append((nx,ny))

    return tmp



while True:
    uni = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                uni.append(search(a, visited, i, j))

    if len(uni) == n**2:
        break

    result += 1
    for i in uni:
        s = 0
        for x,y in i:
            s += a[x][y]

        s //= len(i)

        for x,y in i:
            a[x][y] = s

print(result)
