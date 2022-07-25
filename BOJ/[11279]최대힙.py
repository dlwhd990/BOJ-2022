#https://www.acmicpc.net/problem/11279
#최대 힙 [Silver 2]
import sys
import heapq as hq
I = sys.stdin.readline
q = []


for _ in range(int(I())):
    tmp = int(I())
    if tmp == 0:
        if len(q) == 0:
            print(0)
        else:
            print(abs(hq.heappop(q)))

    else:
        hq.heappush(q,-tmp)