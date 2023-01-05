# 집합의 표현 [Gold 4]
import sys
sys.setrecursionlimit(100000)
I = sys.stdin.readline

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

n,m = map(int,I().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    q,a,b = map(int,I().split())
    if q == 0:
        unionParent(parent,a,b)

    elif q == 1:
        if findParent(parent,a) == findParent(parent,b):
            print("YES")
        else:
            print("NO")
