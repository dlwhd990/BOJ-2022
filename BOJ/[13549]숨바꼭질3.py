#https://www.acmicpc.net/problem/13549
#숨바꼭질3 [Gold 5]
import sys
from collections import deque
I = sys.stdin.readline

n,m = map(int,I().split())

q = deque()
q.append(n)
distance = [int(1e10)]*100001
distance[n] = 0
while q:
    x = q.popleft()
    if x*2 <= 100000 and distance[x*2] == int(1e10):
        distance[x*2] = distance[x]
        q.append(x*2)

    if x > 0 and distance[x-1] == int(1e10):
        distance[x-1] = distance[x] + 1
        q.append(x-1)

    if x < 100000 and distance[x+1] == int(1e10):
        distance[x+1] = distance[x] + 1
        q.append(x+1)

print(distance[m])