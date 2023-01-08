# 지하철 [Gold 2]
import sys
import heapq as hq
I = sys.stdin.readline

n,m = map(int,I().split())
company = []
tmp = []
graph = [[]for _ in range(n)]
distance = [int(1e12)]*n
for _ in range(n):
    company.append(int(I()))

for _ in range(n):
    tmp.append(list(map(int,I().split())))


for i in range(n):
    for j in range(n):
        if tmp[i][j] > 0:
            if company[i] != company[j]:
                graph[i].append((j,int(1e7)+tmp[i][j]))
                graph[j].append((i,int(1e7)+tmp[i][j]))
            else:
                graph[i].append((j,tmp[i][j]))
                graph[j].append((i,tmp[i][j]))



q = []
hq.heappush(q,(0,0))
distance[0] = 0
while q:
    dist,now = hq.heappop(q)
    if distance[now] > dist:
        continue

    for i in graph[now]:
        cost = dist+i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            hq.heappush(q,(cost,i[0]))


print(distance[m]//int(1e7),distance[m]%int(1e7))