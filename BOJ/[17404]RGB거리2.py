#https://www.acmicpc.net/problem/17404
#RGB거리 2 [Gold 4]
import sys
I = sys.stdin.readline

n = int(I())
a = []

for i in range(n):
    a.append(list(map(int,I().split())))
    if i == n-1:
        a.append(a[0])

r = [[int(1e10)]*3 for _ in range(n)] #첫번째 집을 R로 색칠
g = [[int(1e10)]*3 for _ in range(n)] #첫번째 집을 G로 색칠
b = [[int(1e10)]*3 for _ in range(n)] #첫번째 집을 B로 색칠


r[0][0] = a[0][0] #첫번째 집을 R로만 색칠, 나머지 int(1e10)
g[0][1] = a[0][1] #첫번째 집을 G로만 색칠, 나머지 int(1e10)
b[0][2] = a[0][2] #첫번째 집을 B로만 색칠, 나머지 int(1e10)

# 두번째 집을 각각 첫번째 집과 다른 색으로만 칠한다
r[1][1] = r[0][0] + a[1][1]
r[1][2] = r[0][0] + a[1][2]
g[1][0] = g[0][1] + a[1][0]
g[1][2] = g[0][1] + a[1][2]
b[1][0] = b[0][2] + a[1][0]
b[1][1] = b[0][2] + a[1][1]

# 점화식에 따라 각 구간의 최소 가격 구하기
for i in range(2,n):
    r[i][0] = min(r[i-1][1],r[i-1][2]) + a[i][0]
    r[i][1] = min(r[i-1][0],r[i-1][2]) + a[i][1]
    r[i][2] = min(r[i-1][0],r[i-1][1]) + a[i][2]

    g[i][0] = min(g[i-1][1],g[i-1][2]) + a[i][0]
    g[i][1] = min(g[i-1][0],g[i-1][2]) + a[i][1]
    g[i][2] = min(g[i-1][0],g[i-1][1]) + a[i][2]

    b[i][0] = min(b[i-1][1],b[i-1][2]) + a[i][0]
    b[i][1] = min(b[i-1][0],b[i-1][2]) + a[i][1]
    b[i][2] = min(b[i-1][0],b[i-1][1]) + a[i][2]


# 첫번째 집과 마지막 집의 색이 같은 경우를 제외한 결과들 중 최소값 구하기
print(min(min(r[-1][1:]),min(g[-1][0],g[-1][2]),min(b[-1][:2])))