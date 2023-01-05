# 전기가 부족해 [Gold 2]
# point => 발전소들은 모두 루트 취급 => 발전소들은 모두 가상의 노드인 0번 노드와 연결되어 있다고 가정하고 시작 (parent[발전소] = 0로 시작)
import sys
I = sys.stdin.readline

n,m,k = map(int,I().split())
bal = list(map(int,I().split()))
routes = []
result = 0

parent = [i for i in range(n+1)]
for i in bal:
    parent[i] = 0

for _ in range(m):
    a,b,c = map(int,I().split())
    routes.append((a,b,c))

routes.sort(key=lambda x:x[2])

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
        result += cost

print(result)