# 화장실의 규칙 [Gold 4]
import sys
import heapq as hq
I = sys.stdin.readline

result = 0
n,m,k = map(int,I().split())
a = [[]for _ in range(m)]
for i in range(n):
    d,h = map(int,I().split())
    a[i%m].append((-d,-h,i%m,i//m,i))

for i in range(m):
    a[i].reverse()

q = []
for i in range(m):
    if len(a[i]) > 0:
        hq.heappush(q,a[i].pop())

while True:
    out = hq.heappop(q)
    if out[4] == k:
        break

    if len(a[out[2]]) > 0:
        hq.heappush(q,a[out[2]].pop())

    result += 1

print(result)