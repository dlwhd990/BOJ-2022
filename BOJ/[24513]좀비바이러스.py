#https://www.acmicpc.net/problem/24513
#좀비 바이러스 [Gold 3]
import sys
from collections import deque
I = sys.stdin.readline

def simulation(n,m,startList,ground):
    q = deque(startList)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        cnt,x,y,kind = q.popleft()
        if ground[x][y] == "T":
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if ground[nx][ny] == -1 or ground[nx][ny] == "T":
                continue


            if ground[nx][ny] == 0:
                ground[nx][ny] = (kind,cnt+1)
                q.append((cnt+1,nx,ny,kind))

            elif ground[nx][ny][1] == cnt+1 and abs(ground[nx][ny][0]-ground[x][y][0]) == 1:
                ground[nx][ny] = "T"

    return ground



def main():
    ground = []
    q = []
    n,m = map(int,I().split())
    for _ in range(n):
        ground.append(list(map(int,I().split())))

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 or ground[i][j] == 2:
                q.append((0,i,j,ground[i][j]))
                ground[i][j] = (ground[i][j],0)


    result = simulation(n,m,q,ground)
    ans = [0,0,0]

    for i in range(n):
        for j in range(m):
            if result[i][j] == -1 or result[i][j] == 0:
                continue

            if result[i][j] == 'T':
                ans[2] += 1

            elif result[i][j][0] == 1:
                ans[0] += 1

            elif result[i][j][0] == 2:
                ans[1] += 1

    return ans

result = main()
print(*result)