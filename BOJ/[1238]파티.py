# 파티 [Gold 3]
import sys
import heapq as hq

I = sys.stdin.readline

n,m,target = map(int,I().split())
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
        dist,now = hq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                hq.heappush(q,(cost,i[0]))

    return distance

fromTarget = da(target)
result = 0

for i in range(1,n+1):
    dist = da(i)
    result = max(result,dist[target]+fromTarget[i])

print(result)