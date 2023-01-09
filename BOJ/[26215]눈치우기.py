# 눈 치우기 [Silver 3]
import sys
import heapq as hq
I = sys.stdin.readline

n = int(I())
result = 0
tmp = list(map(int,I().split()))
if n == 1:
    if tmp[0] > 1440:
        print(-1)
    else:
        print(tmp[0])
else:
    a = []
    for i in tmp:
        a.append(-i)

    hq.heapify(a)

    while True:
        t1 = hq.heappop(a)
        t2 = hq.heappop(a)

        if t1 == 0:
            break

        else:
            hq.heappush(a,t1+1)
            hq.heappush(a,t2+1)

        result += 1

    if result > 1440:
        print(-1)
    else:
        print(result)