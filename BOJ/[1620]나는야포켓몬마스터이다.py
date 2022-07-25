#https://www.acmicpc.net/problem/1620
#나는야 포켓몬 마스터 이다솜 [Silver 4]
import sys
I = sys.stdin.readline


n,m = map(int,I().split())
a = ['']*(n+1)
d = dict()

for i in range(n):
    tmp = I().rstrip()
    a[i+1] = tmp
    d[tmp] = i+1


for i in range(m):
    tmp = I().rstrip()
    if tmp.isdigit():
        print(a[int(tmp)])
    else:
        print(d[tmp])