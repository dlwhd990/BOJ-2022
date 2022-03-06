# 연속합 [Silver 2]
import sys
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))

d = [0]*n
d[0] = a[0]

for i in range(1,n):
    d[i] = max(d[i-1],d[i])+a[i]

print(max(d))