#https://www.acmicpc.net/problem/14502
#연구소 [Gold 4]

import sys
from collections import deque
from itertools import combinations as com
I = sys.stdin.readline

def search(graph,n,m):
    cnt = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                 q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx,ny))


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1


    return cnt


n,m = map(int,I().split())
a = []
aCopy = [[-1]*m for _ in range(n)]
possible = []

for _ in range(n):
    tmp = list(map(int,I().split()))
    a.append(tmp)


for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            possible.append((i,j))


possibleCom = list(com(possible,3))

result = 0

for one, two, three in possibleCom:

    for i in range(n):
        for j in range(m):
            aCopy[i][j] = a[i][j]

    aCopy[one[0]][one[1]] = 1
    aCopy[two[0]][two[1]] = 1
    aCopy[three[0]][three[1]] = 1
    result = max(result,search(aCopy,n,m))



print(result)


