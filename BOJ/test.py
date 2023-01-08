import sys
I = sys.stdin.readline

n,m = map(int,I().split())
cnt = 2
result = 0
world = []
v = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
routes = []
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


def checkBridge(direction,a,b,c):
    if abs(a-b)-1 < 2:
        return False
    if direction == "vertical":
        for i in range(min(a,b)+1,max(a,b)):
            if world[i][c] != 0:
                return False

    elif direction == 'horizontal':
        for i in range(min(a,b)+1,max(a,b)):
            if world[c][i] != 0:
                return False

    return True



for i in range(n):
    for j in range(m):
        if v[i][j] == 0 and world[i][j] == 1:
            world[i][j] = cnt
            v[i][j] = 1
            dfs(i,j)
            cnt += 1

grounds = [[]for _ in range(cnt)]

for i in range(n):
    for j in range(m):
        if world[i][j] > 1:
            grounds[world[i][j]].append((i,j))



for i in range(2,cnt):
    for j in range(i+1,cnt):
        tmp = []
        for a in grounds[i]:
            dist = 101
            for b in grounds[j]:
                if a[0] == b[0] and checkBridge("horizontal",a[1],b[1],a[0]):
                    dist = min(dist,abs(a[1]-b[1])-1)

                elif a[1] == b[1] and checkBridge("vertical",a[0],b[0],a[1]):
                    dist = min(dist,abs(a[0]-b[0])-1)


            if dist < 101:
                tmp.append(dist)

        if len(tmp) > 0:
            routes.append((i,j,min(tmp)))

routes.sort(key=lambda x:x[2])

def findParent(parent,x):
    if parent[x] != x:
        parent[x] = findParent(parent,parent[x])
    return parent[x]


def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(cnt)]

for now,nxt,cost in routes:
    if findParent(parent,now) != findParent(parent,nxt):
        unionParent(parent,now,nxt)
        result += cost

for i in range(2,cnt):
    findParent(parent,i)

if parent[2:].count(2) != len(parent[2:]):
    print(-1)
else:
    print(result)