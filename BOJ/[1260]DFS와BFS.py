#https://www.acmicpc.net/problem/1260
#DFS와 BFS [Silver5]

import sys
from collections import deque
I = sys.stdin.readline

n,m,v = map(int,I().split())
graph = [[]for _ in range(n+1)]

bfsResult = [v]
dfsResult = [v]

for _ in range(m):
    node_one,node_two = map(int,I().split())
    graph[node_one].append(node_two)
    graph[node_two].append(node_one)

for i in range(1,n+1):
    graph[i].sort()


visitedDfs = [0]*(n+1)
visitedDfs[v] = 1

def dfs(s):
    for g in graph[s]:
        if visitedDfs[g] == 0:
            visitedDfs[g] = 1
            dfsResult.append(g)
            dfs(g)




def bfs(s):
    q = deque()
    q.append(s)
    visited = [0]*(n+1)
    visited[s] = 1
    while q:
        x = q.popleft()
        for g in graph[x]:
            if visited[g] == 1:
                continue
            visited[g] = 1
            bfsResult.append(g)
            q.append(g)

dfs(v)
bfs(v)
print(*dfsResult)
print(*bfsResult)
