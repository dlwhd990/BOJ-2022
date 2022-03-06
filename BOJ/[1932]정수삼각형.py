# 정수 삼각형 [Silver 1]
import sys
I = sys.stdin.readline

n = int(I())
tri = []
d = []

for i in range(n):
    tri.append(list(map(int,I().split())))
    d.append([0]*(i+1))

d[0][0] = tri[0][0]

for i in range(1,n):
    d[i][0] = d[i-1][0] + tri[i][0]
    for j in range(1,len(d[i])-1):
        d[i][j] = tri[i][j] + max(d[i-1][j],d[i-1][j-1])

    d[i][-1] = tri[i][-1] + d[i-1][-1]

print(max(d[-1]))