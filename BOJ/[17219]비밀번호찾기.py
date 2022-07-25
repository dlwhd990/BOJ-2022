#https://www.acmicpc.net/problem/17219
#비밀번호 찾기 [Silver 4]

import sys
I = sys.stdin.readline
d = dict()

n,m = map(int,I().split())

for _ in range(n):
    a,b = I().rstrip().split()
    d[a] = b

for _ in range(m):
    print(d[I().rstrip()])