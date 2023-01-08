# 팀원 모집 [Gold 5]
import sys
from itertools import combinations as com
I = sys.stdin.readline

n,m = map(int,I().split())
a = []
result = 11
for _ in range(m):
    tmp = list(map(int,I().split()))
    a.append(tmp[1:])

p = [i for i in range(m)]
possible = []

for i in range(1,m+1):
    possible.extend(list(com(p,i)))


for i in possible:
    v = [0]*(n+1)
    for j in i:
        for k in a[j]:
            v[k] = 1

    if v.count(0) == 1:
        result = min(result,len(i))


if result == 11:
    print(-1)
else:
    print(result)