# N과 M (2) [Silver 3]
import sys
from itertools import combinations as com
I = sys.stdin.readline

n,m = map(int,I().split())

num = [i for i in range(1,n+1)]

result = list(com(num,m))
for i in result:
    print(*i)