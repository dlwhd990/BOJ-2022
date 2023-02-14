# 두 수의 합 [Silver 3]
import sys
from bisect import bisect_left,bisect_right
I = sys.stdin.readline

result = 0
n = int(I())
a = list(map(int,I().split()))
target = int(I())
a.sort()

for i in range(n):
    now = a[i]
    if bisect_right(a,target-now)-bisect_left(a,target-now) > 0:
        result += 1

print(result//2)