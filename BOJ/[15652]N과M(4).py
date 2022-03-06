# N과 M (4) [Silver 3]
import sys
from itertools import combinations_with_replacement as com
I = sys.stdin.readline

n,m = map(int,I().split())

num = [i for i in range(1,n+1)]

result = list(com(num,m))
for i in result:
    print(*i)