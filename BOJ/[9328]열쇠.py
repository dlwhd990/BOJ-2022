#https://www.acmicpc.net/problem/9328
#열쇠 [Gold 1]

import sys
from collections import deque
I = sys.stdin.readline

def simulation(n,m,ground,hands):
    q = deque()
    q.append((0,0))
    visited = [[0]*(m+2) for _ in range(n+2)]
    visited[0][0] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    opened = [0]*26
    result = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n+1 or ny < 0 or ny > m+1:
                continue

            if visited[nx][ny] == 0:
                if ground[nx][ny] == '.':
                    visited[nx][ny] = 1
                    q.append((nx,ny))

                elif ground[nx][ny] == '*':
                    continue

                elif ground[nx][ny] == '$':
                    result += 1
                    ground[nx][ny] = '.'
                    visited[nx][ny] = 1
                    q.append((nx, ny))

                elif ord(ground[nx][ny]) > 96:
                    if hands[ord(ground[nx][ny])-97] == 0:
                        hands[ord(ground[nx][ny])-97] = 1
                        visited = [[0]*(m+2) for _ in range(n+2)]
                    visited[nx][ny] = 1
                    ground[nx][ny] = '.'
                    q.append((nx,ny))

                elif ord(ground[nx][ny]) < 91 and hands[ord(ground[nx][ny])-65] == 1:
                    if opened[ord(ground[nx][ny])-65] == 0:
                        visited = [[0] * (m + 2) for _ in range(n + 2)]
                        opened[ord(ground[nx][ny])-65] = 1
                    ground[nx][ny] = '.'
                    visited[nx][ny] = 1
                    q.append((nx,ny))


    return result


for _ in range(int(I())):
    n,m = map(int,I().split())
    ground = [["."]*(m+2)]
    for _ in range(n):
        ground.append(["."]+list(I().rstrip())+["."])
    ground.append(["."]*(m+2))
    handsTmp = list(I().rstrip())

    hands = [0]*26
    if handsTmp[0] != '0':
        for i in handsTmp:
            hands[ord(i)-97] = 1

    print(simulation(n,m,ground,hands))