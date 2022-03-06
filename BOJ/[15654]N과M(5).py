# N과 M (5) [Silver 3]
import sys
from itertools import permutations as per
I = sys.stdin.readline

n,m = map(int,I().split())
num = list(map(int,I().split()))

num.sort()

result = list(per(num,m))
for i in result:
    print(*i)