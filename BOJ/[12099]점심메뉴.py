# 점심메뉴 [Gold 4]
import sys
I = sys.stdin.readline

n,q = map(int,I().split())
d = dict()

for _ in range(n):
    e,w = map(int,I().split())
    d[e] = w

for _ in range(q):
    cnt = 0
    u,v,x,y = map(int,I().split())
    for i in range(u,v+1):
        if i in d and x <= d[i] <= y:
            cnt += 1

    print(cnt)