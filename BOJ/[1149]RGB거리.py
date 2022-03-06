# RGB거리 [Silver 1]
import sys
I = sys.stdin.readline

n = int(I())
price = []

for _ in range(n):
    price.append(list(map(int,I().split())))

d = [[int(1e10)]*3 for _ in range(n)]

for i in range(3):
    d[0][i] = price[0][i]

for i in range(1,n):
    d[i][0] = price[i][0] + min(d[i-1][1],d[i-1][2])
    d[i][1] = price[i][1] + min(d[i-1][0],d[i-1][2])
    d[i][2] = price[i][2] + min(d[i-1][0],d[i-1][1])

print(min(d[-1]))