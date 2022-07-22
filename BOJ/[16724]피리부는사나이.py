#https://www.acmicpc.net/problem/16724
#피리 부는 사나이

import sys
I = sys.stdin.readline

n,m = map(int,I().split())
a = []
for _ in range(n):
    a.append(list(I().rstrip()))

cycles = [[-1]*m for _ in range(n)]

def search(graph,cycles,sx,sy):
    global cnt
    x = sx
    y = sy
    tmp = [(x,y)]
    while True:
        if cycles[x][y] == cnt:
            cnt += 1
            return

        if cycles[x][y] != -1:
            for i,j in tmp:
                cycles[i][j] = tmp
            return

        cycles[x][y] = cnt

        if graph[x][y] == 'L':
            y -= 1

        elif graph[x][y] == 'R':
            y += 1

        elif graph[x][y] == 'U':
            x -= 1

        elif graph[x][y] == 'D':
            x += 1

        tmp.append((x,y))


cnt = 0
for i in range(n):
    for j in range(m):
        if cycles[i][j] == -1:
            search(a,cycles,i,j)

print(cnt)