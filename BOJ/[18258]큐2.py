# 큐 2 [Silver 4]
import sys
from collections import deque

I = sys.stdin.readline
n = int(I())
q = deque()
for _ in range(n):
    p = I().rstrip().split()
    if p[0] == "push":
        q.append(p[1])

    elif p[0] == "pop":
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)

    elif p[0] == "size":
        print(len(q))

    elif p[0] == "empty":
        if len(q) > 0:
            print(0)
        else:
            print(1)

    elif p[0] == "front":
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)

    elif p[0] == "back":
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)