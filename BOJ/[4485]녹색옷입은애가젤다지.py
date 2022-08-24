#https://www.acmicpc.net/problem/4485
#녹색 옷 입은 애가 젤다지?
import sys
import heapq as hq
I = sys.stdin.readline

def da(n,ground):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = []
    hq.heappush(q,(ground[0][0],0,0))
    distance = [[int(1e10)]*n for _ in range(n)]
    distance[0][0] = ground[0][0]
    while q:
        dist, x, y = hq.heappop(q)

        if dist > distance[x][y]:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            cost = dist + ground[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                hq.heappush(q,(cost,nx,ny))

    return distance

cnt = 0
while True:
    cnt += 1
    n = int(I())
    if n == 0:
        break
    ground = []
    for _ in range(n):
        ground.append(list(map(int,I().split())))

    distance = da(n,ground)
    print("Problem",cnt,end="")
    print(":",distance[-1][-1])