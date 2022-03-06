# 서강그라운드 [Gold 4]
import sys
import heapq as hq
I = sys.stdin.readline

n,m,r = map(int,I().split())

itemList = list(map(int,I().split()))
graph = [[]for _ in range(n+1)]
for _ in range(r):
    a,b,c = map(int,I().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

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

result = 0

for i in range(1,n+1):
    dist = da(i)
    cnt = 0
    for j in range(1,len(dist)):
        if dist[j] <= m:
            cnt += itemList[j-1]

    result = max(result,cnt)

print(result)