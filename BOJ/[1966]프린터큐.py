#https://www.acmicpc.net/problem/1966
#프린터 큐 [Silver 3]

import sys
from collections import deque
I = sys.stdin.readline

for tc in range(int(I())):
    n,m = map(int,I().split())
    a = list(map(int,I().split()))
    most = max(a)
    q = deque()
    cnt = 0

    for i in range(len(a)):
        q.append((a[i],i))


    while True:
        if q[0][0] == most:
            cnt += 1
            if q[0][1] == m:
                print(cnt)
                break
            q.popleft()

            most = 0
            for value, idx in q:
                most = max(most,value)

        else:
            q.append(q.popleft())