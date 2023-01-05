# 도시 분할 계획 [Gold 4]
import sys
I = sys.stdin.readline

v,e = map(int,I().split())
routes = []
result = []
for _ in range(e):
    a,b,c = map(int,I().split())
    routes.append((a,b,c))

parent = [i for i in range(v+1)]
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


for start,end,cost in routes:
    if findParent(parent,start) != findParent(parent,end):
        unionParent(parent,start,end)
        result.append(cost)

print(sum(result)-max(result))