# 평범한 배낭 [Gold 5]
import sys
I = sys.stdin.readline

n,k = map(int,I().split())
itemList = []

for _ in range(n):
    a,b = map(int,I().split())
    itemList.append((a,b))

bag = [0]*(k+1)

for i in itemList:
    for j in range(k,-1,-1):
        if j-i[0] > -1:
            bag[j] = max(bag[j-i[0]] + i[1],bag[j])

print(max(bag))