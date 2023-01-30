import sys
I = sys.stdin.readline

n = int(I())
move = list(I().rstrip())
sx = 0
sy = 0
d = 2
dx = [-1,0,1,0]
dy = [0,1,0,-1]
route = [[sx,sy]]
for m in move:
    if m == 'F':
        sx += dx[d]
        sy += dy[d]
        route.append([sx,sy])

    elif m == 'R':
        d = (d+1)%4

    elif m == 'L':
        if d == 0:
            d = 3
        else:
            d -= 1


minx = 100
miny = 100
for x,y in route:
    minx = min(minx,x)
    miny = min(miny,y)

for i in range(len(route)):
    route[i][0] -= minx
    route[i][1] -= miny

maxx = 0
maxy = 0

for x,y in route:
    maxx = max(maxx,x)
    maxy = max(maxy,y)

result = [['#']*(maxy+1) for _ in range(maxx+1)]

for x,y in route:
    result[x][y] = '.'

for i in result:
    print(''.join(i))