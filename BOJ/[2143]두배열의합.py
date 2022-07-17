#https://www.acmicpc.net/problem/2143
#두 배열의 합 [Gold 3]

import sys
from bisect import bisect_left,bisect_right
I = sys.stdin.readline

target = int(I())
n = int(I())
a = list(map(int,I().split()))
m = int(I())
b = list(map(int,I().split()))

ap = [0]
bp = [0]

ar = []
br = []

for i in range(n):
    ap.append(ap[-1]+a[i])

for i in range(m):
    bp.append(bp[-1]+b[i])

for i in range(n+1):
    for j in range(i+1,n+1):
        tmp = ap[j]-ap[i]
        ar.append(tmp)

for i in range(m+1):
    for j in range(i+1,m+1):
        tmp = bp[j]-bp[i]
        br.append(tmp)


ar.sort()
result = 0

for i in br:
    t = target-i
    result += (bisect_right(ar,t)- bisect_left(ar,t))

print(result)