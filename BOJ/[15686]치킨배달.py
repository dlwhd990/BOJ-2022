# 치킨 배달 [Gold 5]
import sys
from itertools import combinations as com
I = sys.stdin.readline

n,m = map(int,I().split())
ground = []
chickenList = []
homeList = []

for _ in range(n):
    ground.append(list(map(int,I().split())))

for i in range(n):
    for j in range(n):
        if ground[i][j] == 2:
            chickenList.append((i,j))

        elif ground[i][j] == 1:
            homeList.append((i,j))

chickenCom = list(com([i for i in range(len(chickenList))],m))

result = int(1e10)
for i in chickenCom:
    miniSum = 0
    for hx,hy in homeList:
        minimum = int(1e10)
        for idx in i:
            minimum = min(minimum,abs(hx-chickenList[idx][0])+abs(hy-chickenList[idx][1]))
        miniSum += minimum

    result = min(result,miniSum)

print(result)