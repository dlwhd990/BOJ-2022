# 최소비용 구하기 [Gold 5]
import sys
import heapq as hq
I = sys.stdin.readline

n = int(I())
m = int(I())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,I().split())
    graph[a].append((b,c))

start, dest = map(int,I().split())

q = []
hq.heappush(q,(0,start))
distance = [int(1e10)]*(n+1)
distance[start] = 0
while q:
    dist,now = hq.heappop(q)
    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = i[1] + dist
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            hq.heappush(q,(cost,i[0]))

print(distance[dest])