# 골목길 [Gold 2]
import sys
from collections import deque
I = sys.stdin.readline
INF = int(1e10)

n,m = map(int,I().split())
distance = [-INF]*(n+1)
graph = [[]for _ in range(n+1)]
route = []
r = [[]for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,I().split())
    graph[a].append(b)
    route.append((a,b,c))


# bfs로 이동 가능한 곳인지 판별
possible = [[]]

for i in range(1,n+1):
    q = deque()
    q.append(i)
    bfsDist = [-1]*(n+1)
    bfsDist[i] = 0

    while q:
        s = q.popleft()
        for x in graph[s]:
            if bfsDist[x] == -1:
                bfsDist[x] = bfsDist[s]+1
                q.append(x)

    possible.append(bfsDist)


def bellman():
    distance[1] = 0
    for i in range(n):
        for now, nxt, cost in route:
            if distance[now] != -INF and distance[now]+cost > distance[nxt]:
                distance[nxt] = distance[now]+cost
                if i == n-1 and (now in r[n] or possible[now][n] != -1):
                    return False

                if len(r[nxt]) < n+1:
                    r[nxt] = r[now]+[now]

    return True

if not bellman():
    print(-1)

else:
    print(*r[-1],n)