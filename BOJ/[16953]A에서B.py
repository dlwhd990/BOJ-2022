# A → B [Silver 1]
import sys
from collections import deque
I = sys.stdin.readline

n,m = map(int,I().split())
check = 0

q = deque()
q.append((1,n))
while q:
    dist, now = q.popleft()
    if now == m:
        print(dist)
        check = 1
        break
    if now*2 <= int(1e9):
        q.append((dist+1,now*2))

    if now*10+1 <= int(1e9):
        q.append((dist+1,now*10+1))

if check == 0:
    print(-1)