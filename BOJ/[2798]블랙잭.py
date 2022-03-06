# 블랙잭 [Bronze 2]
import sys
from itertools import combinations as com
I = sys.stdin.readline

n,m = map(int,I().split())
a = list(map(int,I().split()))

r = list(com(a,3))

result = 0
for i in r:
    s = sum(i)
    if s > m:
        continue

    result = max(result,s)

print(result)