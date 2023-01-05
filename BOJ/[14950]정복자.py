# 정복자 [Gold 3]
import sys
I = sys.stdin.readline

n,m,t = map(int,I().split())
routes = []
cnt = 0
result = 0
for _ in range(m):
    a,b,c = map(int,I().split())
    routes.append((a,b,c))

routes.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]

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
        result += (cost+cnt*t)
        cnt += 1

print(result)