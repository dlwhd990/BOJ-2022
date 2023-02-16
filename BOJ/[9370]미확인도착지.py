import sys
import heapq as hq
I = sys.stdin.readline

def da(n,s,graph):
    q = []
    hq.heappush(q,(0,s))
    distance = [int(1e10)]*(n+1)
    distance[s] = 0
    while q:
        dist,now = hq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1]+dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                hq.heappush(q,(cost,i[0]))

    return distance

for _ in range(int(I())):
    n,m,t = map(int,I().split())
    s,g,h = map(int,I().split())
    graph = [[]for _ in range(n+1)]
    result = []

    for _ in range(m):
        a,b,c = map(int,I().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    original = da(n, s, graph)
    startToOne = original[g]
    startToTwo = original[h]
    fromOne = da(n,g,graph)
    oneToTwo = fromOne[h]
    fromTwo = da(n,h,graph)

    for _ in range(t):
        hubo = int(I())
        if original[hubo] == startToOne+oneToTwo+fromTwo[hubo]:
            result.append(hubo)

        elif original[hubo] == startToTwo+oneToTwo+fromOne[hubo]:
            result.append(hubo)

    result.sort()
    print(*result)