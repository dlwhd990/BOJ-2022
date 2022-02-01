#https://www.acmicpc.net/problem/12851
#숨바꼭질2 [Gold 5]
import sys
from collections import deque
I = sys.stdin.readline

n,m = map(int,I().split())
distance = [int(1e10)]*100001

q = deque()
q.append(n)
distance[n] = 0
cnt = [0]*100001

while q:
    x = q.popleft()
    if x > 0 and distance[x-1] >= distance[x] + 1:
        distance[x-1] = distance[x] + 1
        q.append(x-1)
        cnt[x-1] += 1

    if x < 100000 and distance[x+1] >= distance[x] + 1:
        distance[x+1] = distance[x] + 1
        q.append(x+1)
        cnt[x+1] += 1

    if x*2 <= 100000 and distance[x*2] >= distance[x] + 1:
        distance[x*2] = distance[x] + 1
        q.append(x*2)
        cnt[x*2] += 1

print(distance[m])
if n == m:
    print(1)
else:
    print(cnt[m])