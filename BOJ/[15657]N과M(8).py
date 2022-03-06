# N과 M (8) [Silver 3]
import sys
from itertools import combinations_with_replacement as com
I = sys.stdin.readline

n,m = map(int,I().split())
num = list(map(int,I().split()))

num.sort()

result = list(com(num,m))
for i in result:
    print(*i)