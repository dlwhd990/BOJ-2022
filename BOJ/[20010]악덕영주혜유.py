# 악덕 영주 혜유 [Gold 2]
import sys
import heapq as hq
I = sys.stdin.readline

n,m = map(int,I().split())
routes = []
result = 0
farthest = 0

for _ in range(m):
    a,b,c = map(int,I().split())
    routes.append((a,b,c))


routes.sort(key=lambda x:x[2])
graph = [[]for _ in range(n)]
parent = [i for i in range(n)]


def find(parent,x):
    if x != parent[x]:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def da(s):
    distance = [int(1e10)]*n
    distance[s] = 0
    q = []
    hq.heappush(q,(0,s))
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                hq.heappush(q,(cost,i[0]))

    return distance

for a,b,cost in routes:
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        graph[a].append((b,cost))
        graph[b].append((a,cost))
        result += cost


for i in range(n):
    farthest = max(farthest,max(da(i)))

print(result)
print(farthest)