#https://www.acmicpc.net/problem/1697
#숨바꼭질 [Silver 5]
import sys
from collections import deque
I = sys.stdin.readline

n,m = map(int,I().split())
distance = [-1]*100001

q = deque()
q.append(n)
distance[n] = 0
while q:
    x = q.popleft()
    if x > 0 and distance[x-1] == -1:
        distance[x-1] = distance[x] + 1
        q.append(x-1)

    if x < 100000 and distance[x+1] == -1:
        distance[x+1] = distance[x] + 1
        q.append(x+1)

    if x*2 <= 100000 and distance[x*2] == -1:
        distance[x*2] = distance[x] + 1
        q.append(x*2)

print(distance[m])