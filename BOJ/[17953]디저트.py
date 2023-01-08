# 디저트 [Gold 5]
import sys
I = sys.stdin.readline
a = []
n,m = map(int,I().split())
for _ in range(m):
    a.append(list(map(int,I().split())))

d = [[0]*m for _ in range(n)]

for i in range(m):
    d[0][i] = a[i][0]


for i in range(1,n):
    if m == 1:
        d[i][0] = d[i-1][0] + (a[0][i]//2)
        continue
    for j in range(m):
        d[i][j] = max(max(d[i-1][:j] + d[i-1][j+1:])+a[j][i],d[i-1][j]+(a[j][i]//2))

print(max(d[-1]))