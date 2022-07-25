#https://www.acmicpc.net/problem/2606
#바이러스 [Silver 3]

import sys
I = sys.stdin.readline

n = int(I())
m = int(I())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,I().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

def dfs(s):
    visited[s] = 1

    for i in graph[s]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(visited.count(1)-1)