# 웜홀 [Gold 3]
import sys
I = sys.stdin.readline
INF = int(1e10)


def bellman(start):
    distance[start] = 0

    for i in range(n):
        for now,nxt,cost in routes:
            if distance[now]+cost < distance[nxt]:
                distance[nxt] = distance[now]+cost
                # print(i==n-1,now,nxt,cost,distance)
                if i == n-1:
                    return False

    return True


for _ in range(int(I())):
    n,m,w = map(int,I().split())
    routes = []
    distance = [INF]*(n+1)
    for _ in range(m):
        s,e,t = map(int,I().split())
        routes.append((s,e,t))
        routes.append((e,s,t))

    for _ in range(w):
        s,e,t = map(int,I().split())
        routes.append((s,e,-t))

    routes.sort(key=lambda x:x[0])

    if bellman(1):
        print("NO")
    else:
        print("YES")
