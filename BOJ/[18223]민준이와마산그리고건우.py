#https://www.acmicpc.net/problem/18223
#민준이와 마산 그리고 건우 [Gold 4]
import sys
import heapq as hq
I = sys.stdin.readline

n,m,gun = map(int,I().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,I().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

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
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))

    return distance

fromOne = da(1)
fromGunwoo = da(gun)

if fromOne[n] == fromOne[gun] + fromGunwoo[n]:
    print("SAVE HIM")

else:
    print("GOOD BYE")