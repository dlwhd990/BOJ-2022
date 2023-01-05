# 타임머신 [Gold 4]

import sys
I = sys.stdin.readline
INF = int(1e10)

n,m = map(int,I().split())
routes = []
distance = [INF]*(n+1)
for _ in range(m):
    a,b,c = map(int,I().split())
    routes.append((a,b,c))


def bellmanFord(start):
    distance[start] = 0

    for i in range(n):
        for now,nxt,cost in routes:
            if distance[now] != INF and distance[now]+cost < distance[nxt]:
                distance[nxt] = distance[now]+cost
                if i == n-1:
                    return False


    return True


if not bellmanFord(1):
    print(-1)

else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])