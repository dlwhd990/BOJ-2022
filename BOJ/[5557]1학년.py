# 1학년 [Gold 5]

import sys
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))
target = a.pop()

d = [[0]*21 for _ in range(len(a))]

d[0][a[0]] = 1

for i in range(1,len(a)):
    for j in range(21):
        if j-a[i] >= 0 and d[i-1][j-a[i]] > 0:
            d[i][j] += d[i-1][j-a[i]]
        if j+a[i] <= 20 and d[i-1][j+a[i]] > 0:
            d[i][j] += d[i-1][j+a[i]]

print(d[-1][target])