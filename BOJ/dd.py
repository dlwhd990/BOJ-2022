import sys
I = sys.stdin.readline

n,m = map(int,I().split())
world = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
route = []
v = [[0]*m for _ in range(n)]
cnt = 2
dist = 0

for _ in range(n):
    world.append(list(map(int,I().split())))


def dfs(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue

        if v[nx][ny] == 0 and world[nx][ny] == 1:
            v[nx][ny] = 1
            world[nx][ny] = cnt
            dfs(nx,ny)


for i in range(n):
    for j in range(m):
        if world[i][j] == 1 and v[i][j] == 0:
            world[i][j] = cnt
            dfs(i,j)
            cnt += 1

for i in world:
    print(*i)

r = [[]for _ in range(cnt)]

for i in range(n):
    for j in range(m):
        if world[i][j] > 1:
            r[world[i][j]].append((i,j))


# 문제 => 섬간 거리 1인 경우, 다리 없어야 되는데 그 뒤에 거리 2인 곳의 땅 때문에 2짜리 다리 만들어짐
# 1짜리 다리 생성 가능한 경우 두 섬 비교 그만두기

for i in range(2,cnt):
    for j in range(i+1,cnt):
        dist = 101
        check = 0
        tmp = []
        for a in r[i]:
            for b in r[j]:
                if a[0] == b[0]:
                    if abs(a[1]-b[1])-1 <= 1:
                        check = 1
                        break
                    tmp.append(abs(a[1]-b[1])-1)
                elif a[1] == b[1]:
                    if abs(a[0]-b[0])-1 <= 1:
                        check = 1
                        break
                    tmp.append(abs(a[0]-b[0])-1)

                print("TMP",i,j,a,b,tmp)
        print("FINAL",i,j,check)
        if check == 1:
            continue
        elif len(tmp) > 0:
            dist = min(dist,min(tmp))



        if dist == 101:
            continue

        route.append((i,j,dist))

print(route)