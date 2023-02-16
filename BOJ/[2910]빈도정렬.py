import sys
I = sys.stdin.readline

n,m = map(int,I().split())
d = dict()
a = list(map(int,I().split()))
r = []
idx = 0

for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

for key in d.keys():
    r.append((d[key],idx,key))
    idx += 1

r.sort(key=lambda x:(-x[0],x[1]))

for i in range(len(r)):
    for j in range(r[i][0]):
        print(r[i][2],end=' ')