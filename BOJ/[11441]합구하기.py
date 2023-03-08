import sys
I = sys.stdin.readline

n = int(I())
k = list(map(int,I().split()))
m = int(I())
pre = [0]

for i in range(n):
    pre.append(pre[-1]+k[i])


for _ in range(m):
    a,b = map(int,I().split())
    print(pre[b]-pre[a-1])