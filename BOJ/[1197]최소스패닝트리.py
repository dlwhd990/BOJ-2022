# 최소 스패닝 트리 [Gold 4]
import sys
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



v,e = map(int,I().split())
routes = []
result = 0

for _ in range(e):
    a,b,c = map(int,I().split())
    routes.append((a,b,c))

parent = [i for i in range(v+1)]
routes.sort(key=lambda x:x[2])

for a,b,c in routes:
    if findParent(parent,a) != findParent(parent,b):
        unionParent(parent,a,b)
        result += c

print(result)
