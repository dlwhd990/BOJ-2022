#https://www.acmicpc.net/problem/1927
#최소 힙 [Silver 2]

import sys
import heapq as hq
I = sys.stdin.readline
q = []
hq.heapify(q)

for _ in range(int(I())):
    n = int(I())
    if n == 0:
        if len(q) == 0:
            print(0)

        else:
            print(hq.heappop(q))

    else:
        hq.heappush(q,n)