# 친구 네트워크 [Gold 2]
import sys
I = sys.stdin.readline

def findParent(parent,x):
    if x != parent[x]:
        parent[x] = findParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(I())):
    n = int(I())
    fList = []
    d = dict()
    t = dict()
    cnt = 0

    for _ in range(n):
        a,b = I().rstrip().split()
        fList.append((a,b))
        if a not in d:
            cnt += 1
            d[a] = cnt

        if b not in d:
            cnt += 1
            d[b] = cnt

    parent = [i for i in range(cnt+1)]
    k = [0]*(cnt+1)

    for a,b in fList:
        r = 0
        if a in t:
            t[a] = findParent(parent,d[a])
        if b in t:
            t[b] = findParent(parent,d[b])
        unionParent(parent,d[a],d[b])
        aResult = findParent(parent,d[a])
        bResult = findParent(parent,d[b])

        # print(a,b,aResult,bResult,t)
        if a not in t:
            t[a] = aResult
            k[aResult] += 1

        elif t[a] != aResult:
            k[aResult] += k[t[a]]
            k[t[a]] = 0
            t[a] = aResult

        if b not in t:
            t[b] = bResult
            k[bResult] += 1

        elif t[b] != bResult:
            k[bResult] += k[t[b]]
            k[t[b]] = 0
            t[b] = aResult

        print(k[aResult])
        # print(d[a],d[b],aResult,bResult)
        # print(k)
        # print("-----")


# 1
# 10
# a b
# c d
# e f
# g h
# i j
# h f
# j h
# f h
# e h
# i a