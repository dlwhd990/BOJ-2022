# 군사 이동 [Gold 3]
import sys
I = sys.stdin.readline

n,m = map(int,I().split())
start,end = map(int,I().split())
routes = []
parent = [i for i in range(n)]
result = []

for _ in range(m):
    a,b,c = map(int,I().split())
    routes.append((a,b,c))

routes.sort(key=lambda x:-x[2])

def findParent(parent,x):
    if x != parent[x]:
        parent[x] = findParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for a,b,cost in routes:
    if findParent(parent,a) != findParent(parent,b):
        unionParent(parent,a,b)
        result.append(cost)
        if findParent(parent,start) == findParent(parent,end):
            break

print(min(result))