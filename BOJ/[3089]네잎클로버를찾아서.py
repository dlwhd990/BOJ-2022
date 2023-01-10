# 네잎 클로버를 찾아서 [Gold 3]
import sys
from bisect import bisect_left,bisect_right
I = sys.stdin.readline

n,m = map(int,I().split())
nx = ny = 0
d = dict()
t = dict()
for _ in range(n):
    x,y = map(int,I().split())
    if x not in d:
        d[x] = [y]
    else:
        d[x].append(y)

    if y not in t:
        t[y] = [x]
    else:
        t[y].append(x)

for key in d.keys():
    d[key].sort()

for key in t.keys():
    t[key].sort()


move = list(I().rstrip())

for i in move:
    if i == 'U':
        ny = d[nx][bisect_right(d[nx],ny)]

    elif i == 'D':
        ny = d[nx][bisect_left(d[nx],ny)-1]

    elif i == 'L':
        nx = t[ny][bisect_left(t[ny],nx)-1]

    elif i == 'R':
        nx = t[ny][bisect_right(t[ny],nx)]

print(nx,ny)