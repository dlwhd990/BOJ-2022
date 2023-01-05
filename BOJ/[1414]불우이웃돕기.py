# 불우이웃돕기 [Gold 3]
import sys
I = sys.stdin.readline

def convertToLength(c):
    if 97 <= ord(c):
        return ord(c)-96
    else:
        return ord(c)-38


n = int(I())
graph = []
routes = []
result = 0
total = 0
for _ in range(n):
    graph.append(list(I().rstrip()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == '0':
            continue

        total += convertToLength(graph[i][j])
        if i != j:
            routes.append((i,j,convertToLength(graph[i][j])))



routes.sort(key=lambda x:x[2])
parent = [i for i in range(n)]

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


for a,b,cost in routes:
    if findParent(parent,a) != findParent(parent,b):
        unionParent(parent,a,b)
        result += cost

for i in range(n):
    findParent(parent,i)

if len(list(set(parent))) > 1:
    print(-1)
else:
    print(total-result)