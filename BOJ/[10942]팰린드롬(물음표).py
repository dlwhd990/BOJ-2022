#https://www.acmicpc.net/problem/10942
#팰린드롬? [Gold 4]

import sys
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))

t = [[0]*n for _ in range(n)]

for i in range(n):
    t[i][i] = 1

for i in range(1,n):
    for j in range(1,n):
        if i-j < 0 or i+j > n-1:
            break

        if a[i-j] == a[i+j]:
            t[i-j][i+j] = 1

        else:
            break

for i in range(1,n):
    for j in range(n):
        if i-1-j < 0 or i+j > n-1:
            break

        if a[i-1-j] == a[i+j]:
            t[i-1-j][i+j] = 1

        else:
            break


for _ in range(int(I())):
    left,right = map(int,I().split())
    print(t[left-1][right-1])