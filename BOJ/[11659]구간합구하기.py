# 구간 합 구하기 4 [Silver 3]
import sys
I = sys.stdin.readline

n,m = map(int,I().split())
num = list(map(int,I().split()))
prefix = [0]

for i in range(n):
    prefix.append(prefix[-1]+num[i])

for _ in range(m):
    a,b = map(int,I().split())
    print(prefix[b]-prefix[a-1])