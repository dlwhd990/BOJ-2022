# 여행 가자 [Gold 4]
import sys
I = sys.stdin.readline

n = int(I())
m = int(I())
graph = []
routes = []
parent = [i for i in range(n+1)]
for _ in range(n):
    graph.append(list(map(int,I().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            routes.append((i+1,j+1))


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


for a,b in routes:
    unionParent(parent,a,b)


order = list(map(int,I().split()))

def result():
    for i in range(m - 1):
        if findParent(parent, order[i]) != findParent(parent, order[i + 1]):
            return "NO"

    return "YES"

print(result())