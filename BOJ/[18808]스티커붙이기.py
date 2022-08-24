#https://www.acmicpc.net/problem/18808
#스티커 붙이기 [Gold 3]

#보류
import sys
I = sys.stdin.readline

n,m,k = map(int,I().split())
notebook = [[0]*m for _ in range(n)]

for _ in range(k):
    x,y = map(int,I().split())
    sticker = []
    for _ in range(x):
        sticker.append(list(map(int,I().split())))

     for i in range(x):
         for j in range(y):
             if sticker[i][j] == 1:


    for i in range(n):
        if i+x > n:
            break
        for j in range(m):
            if j+y > m:
                break


