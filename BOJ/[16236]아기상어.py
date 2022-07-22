#https://www.acmicpc.net/problem/16236
#아기 상어 [Gold 3]

import sys
from collections import deque
I = sys.stdin.readline

n = int(I())
a = []
sx = -1
sy = -1
level = 2
exp = 0
result = 0

for _ in range(n):
    a.append(list(map(int,I().split())))


for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            sx = i
            sy = j
            a[i][j] = 0

def bfs(graph,sx,sy):
    global level, exp
    q = deque()
    q.append((sx,sy))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    distance = [[-1]*n for _ in range(n)]
    distance[sx][sy] = 0
    possibleFish = []
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue


            if graph[nx][ny] <= level and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                if graph[nx][ny] != 0 and graph[nx][ny] < level:
                    possibleFish.append((distance[nx][ny],nx,ny))
                q.append((nx,ny))

    if len(possibleFish) == 0:
        return False
    possibleFish.sort(key=lambda x:(x[0],x[1],x[2]))
    return possibleFish[0]


while True:
    r = bfs(a,sx,sy)

    if r == False:
        print(result)
        break
    result += r[0]
    sx = r[1]
    sy = r[2]
    exp += 1
    if exp == level:
        exp = 0
        level += 1
    a[r[1]][r[2]] = 0