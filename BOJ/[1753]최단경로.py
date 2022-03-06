# 최단경로 [Gold 5]
import sys
import heapq as hq
I = sys.stdin.readline

n,m = map(int,I().split())
start = int(I())

graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,I().split())
    graph[a].append((b,c))


def da(s):
    q = []
    hq.heappush(q,(0,s))
    distance = [int(1e10)]*(n+1)
    distance[s] = 0
    while q:
        dist, now = hq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q,(cost,i[0]))

    return distance

result = da(start)

for i in range(1,len(result)):
    if result[i] == int(1e10):
        print("INF")
    else:
        print(result[i])