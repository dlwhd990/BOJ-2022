#https://www.acmicpc.net/problem/9694
#무엇을 아느냐가 아니라 누구를 아느냐가 문제다  [Gold 3]
import sys
import heapq as hq
I = sys.stdin.readline

def da(t,n,graph):
    q = []
    route = []
    hq.heappush(q,([0],0,0))
    distance = [int(1e10)]*(n)
    distance[0] = 0
    while q:
        r, dist, now = hq.heappop(q)
        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q,(r+[i[0]],cost,i[0]))
                if i[0] == n-1:
                    route.append((cost,r+[i[0]]))

    if distance[-1] == int(1e10):
        print("Case","#"+str(t+1)+":",-1)
        return

    route.sort()
    print("Case", "#" + str(t+1) + ":", end=" ")
    print(*route[0][1])
    return



for t in range(int(I())):
    n,m = map(int,I().split()
    graph = [[]for _ in range(m)]
    for _ in range(n):
        a,b,c = map(int,I().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    da(t,m,graph)