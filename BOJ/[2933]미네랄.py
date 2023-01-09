# 미네랄 [Gold 2]
import sys
sys.setrecursionlimit(100000)
I = sys.stdin.readline

n,m = map(int,I().split())
a = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    a.append(list(I().rstrip()))

cnt = int(I())
b = list(map(int,I().split()))

def shoot(height,start):
    if start%2 == 0:
        for i in range(m):
            if a[height][i] == 'x':
                a[height][i] = '.'
                break

    else:
        for i in range(m-1,-1,-1):
            if a[height][i] == 'x':
                a[height][i] = '.'
                break


def dfs(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue

        if a[nx][ny] == 'x' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            tmp.append([nx,ny])
            dfs(nx,ny)




for i in range(cnt):
    shoot(n-b[i],i)
    visited = [[0] * m for _ in range(n)]
    cluster = []
    check = [0,0]
    groundCheck = 0
    for x in range(n):
        for y in range(m):
            if a[x][y] == 'x' and visited[x][y] == 0:
                tmp = [[x,y]]
                visited[x][y] = 1
                dfs(x,y)
                cluster.append(tmp)


    if len(cluster) <= 1:
        continue

    for j in range(2):
        for c in cluster[j]:
            if c[0] == n-1:
                check[j] = 1

    if check.count(1) == 1:
        fall = check.index(0)
        for p in cluster[fall]:
            a[p[0]][p[1]] = '.'

        while True:
            for j in range(len(cluster[fall])):
                cluster[fall][j][0] += 1
                if cluster[fall][j][0] == n-1:
                    groundCheck = 1

            if groundCheck == 1:
                break

            for j in range(len(cluster[fall])):
                if a[cluster[fall][j][0]+1][cluster[fall][j][1]] == 'x':
                    groundCheck = 1
                    break

            if groundCheck == 1:
                break


        for x,y in cluster[fall]:
            a[x][y] = 'x'

for i in a:
    print(''.join(i))