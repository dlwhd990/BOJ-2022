# 계단 오르기 [Silver 3]
import sys
I = sys.stdin.readline

n = int(I())
stairs = []
for _ in range(n):
    stairs.append(int(I()))

d = [0]*n

if n < 3:
    print(sum(stairs))
else:
    d[0] = stairs[0]
    d[1] = stairs[0]+stairs[1]
    d[2] = max(stairs[0],stairs[1])+stairs[2]

    for i in range(3,n):
        d[i] = max(d[i-3]+stairs[i-1],d[i-2]) + stairs[i]

    print(d[-1])