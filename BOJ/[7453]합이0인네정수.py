# 합이 0인 네 정수 [Gold 2]
import sys
I = sys.stdin.readline

n = int(I())
a = []
b = []
c = []
d = []
two = dict()
result = 0
for _ in range(n):
    q,w,e,r = map(int,I().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)

for i in range(n):
    for j in range(n):
        tmp = a[i]+b[j]
        if tmp in two:
            two[tmp] += 1
        else:
            two[tmp] = 1

for i in range(n):
    for j in range(n):
        tmp = -(c[i]+d[j])
        if (tmp in two):
            result += two[tmp]

print(result)