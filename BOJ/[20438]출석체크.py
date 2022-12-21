# 출석체크 [Silver 2]
import sys
I = sys.stdin.readline

n,k,q,m = map(int,I().split())
jol = list(map(int,I().split()))
rec = list(map(int,I().split()))

chul = [0]*(n+3)
jolList = [0]*(n+3)

table = [[0]*(n+3) for _ in range(n+3)]

for i in jol:
    jolList[i] = 1


for i in range(len(rec)):
    tmp = rec[i]
    if jolList[tmp] == 1:
        continue
    t = 0
    while tmp*(t+1) < n+3:
        t += 1
        if jolList[tmp*t] == 1:
            continue
        chul[tmp*t] = 1


for i in range(3,n+3):
    cnt = 0
    if chul[i] == 0:
        cnt += 1
    for j in range(i+1,n+3):
        if chul[j] == 0:
            cnt += 1

        table[i][j] = cnt


for _ in range(m):
    s,e = map(int,I().split())
    print(table[s][e])