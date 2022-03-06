# N과 M (9) [Silver 2]
import sys
from itertools import permutations as per
I = sys.stdin.readline

n,m = map(int,I().split())
num = list(map(int,I().split()))

num.sort()

result = list(per(num,m))
result = list(set(result))
result.sort()
for i in result:
    print(*i)