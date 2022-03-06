# 특정한 최단 경로 [Gold 4]
import sys
import heapq as hq
I = sys.stdin.readline

n,e = map(int,I().split())

graph = [[]for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,I().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

mustA,mustB = map(int,I().split())

def da(s):
    q = []
    hq.heappush(q, (0, s))
    distance = [int(1e10)] * (n + 1)
    distance[s] = 0

    while q:
        dist, now = hq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))

    return distance

fromStart = da(1)
fromMustA = da(mustA)
fromMustB = da(mustB)

resultA = fromStart[mustA] + fromMustA[mustB] + fromMustB[n]
resultB = fromStart[mustB] + fromMustB[mustA] + fromMustA[n]

if min(resultA,resultB) >= int(1e10):
    print(-1)
else:
    print(min(resultA,resultB))