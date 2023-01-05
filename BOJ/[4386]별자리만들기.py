# 별자리 만들기 [Gold 3]
import sys
import math
I = sys.stdin.readline


n = int(I())
result = 0
routes = []
parent = [i for i in range(n)]
positions = []
for _ in range(n):
    a,b = map(float,I().split())
    positions.append((a,b))


for i in range(n):
    ax = positions[i][0]
    ay = positions[i][1]
    for j in range(i+1,n):
        bx = positions[j][0]
        by = positions[j][1]
        routes.append((i,j,math.sqrt((ax-bx)**2 + (ay-by)**2)))
        routes.append((j,i,math.sqrt((ax-bx)** 2 + (ay-by)**2)))

routes.sort(key=lambda x:x[2])

def findPaernt(parent,x):
    if parent[x] != x:
        parent[x] = findPaernt(parent,parent[x])
    return parent[x]


def unionParent(parent,a,b):
    a = findPaernt(parent,a)
    b = findPaernt(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b



for start,end,cost in routes:
    if findPaernt(parent,start) != findPaernt(parent,end):
        unionParent(parent,start,end)
        result += cost

print(result)