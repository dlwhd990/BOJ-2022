# 학교 탐방하기 [Gold 3]
import sys
I = sys.stdin.readline

n,m = map(int,I().split())
good = bad = 0
goodRoutes = []
badRoutes = []
goodParent = [i for i in range(n+1)]
badParent = [i for i in range(n+1)]

for _ in range(m+1):
    a,b,c = map(int,I().split())
    goodRoutes.append((a,b,abs(c-1)))
    badRoutes.append((a,b,c))

goodRoutes.sort(key=lambda x:x[2])
badRoutes.sort(key=lambda x:x[2])

def findParent(parent,x):
    if parent[x] != x:
        parent[x] = findParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for start,end,cost in goodRoutes:
    if findParent(goodParent,start) != findParent(goodParent,end):
        unionParent(goodParent,start,end)
        good += cost

for start,end,cost in badRoutes:
    if findParent(badParent,start) != findParent(badParent,end):
        unionParent(badParent,start,end)
        bad += cost

print((n-bad)**2 - good**2)