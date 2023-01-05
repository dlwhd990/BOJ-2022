# 우주신과의 교감 [Gold 3]
import sys
import math
I = sys.stdin.readline

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

n,m = map(int,I().split())
p = []
parent = [i for i in range(n+1)]
routes = []
result = 0
for _ in range(n):
    a,b = map(int,I().split())
    p.append((a,b))

for i in range(n):
    for j in range(i+1,n):
        routes.append((i+1,j+1,math.sqrt((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)))
        routes.append((j+1,i+1,math.sqrt((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)))

routes.sort(key=lambda x:x[2])

for _ in range(m):
    a,b = map(int,I().split())
    unionParent(parent,a,b)


for start,end,cost in routes:
    if findParent(parent,start) != findParent(parent,end):
        unionParent(parent,start,end)
        result += cost

print("{:.2f}".format(result))