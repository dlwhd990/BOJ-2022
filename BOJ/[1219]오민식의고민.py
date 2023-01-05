# 오민식의 고민 [Gold 1]

import sys
from collections import deque
I = sys.stdin.readline
INF = int(1e15)

def main():
    n,start,end,m = map(int, I().split())
    routes = []
    graph = [[]for _ in range(n)]
    distance = [-INF] * n
    possible = []

    for _ in range(m):
        a, b, c = map(int, I().split())
        routes.append([a, b, -c])
        graph[a].append(b)

    earnList = list(map(int, I().split()))


    for i in range(m):
        routes[i][2] += earnList[routes[i][1]]


    def bfs(start):
        q = deque()
        q.append(start)
        visited = [0]*n
        visited[start] = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)

        return visited

    for i in range(n):
        possible.append(bfs(i))

    def bellman():
        distance[start] = earnList[start]

        for i in range(n):
            for now, nxt, cost in routes:
                if distance[now] != -INF and distance[now]+cost > distance[nxt]:
                    distance[nxt] = distance[now] + cost
                    if i == n-1 and possible[nxt][end] == 1:
                        return True

        return False

    isCycle = bellman()

    if distance[end] == -INF:
        return "gg"

    if isCycle:
        return "Gee"

    return distance[end]

print(main())

# 6 0 2 6
# 0 1 10
# 1 2 10
# 0 3 1
# 3 4 1
# 4 5 1
# 5 3 1
# 10 5 5 100 100 100
