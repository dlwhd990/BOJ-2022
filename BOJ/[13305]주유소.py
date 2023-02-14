# 주유소 [Silver 3]

import sys
I = sys.stdin.readline

result = 0
n = int(I())
distance = list(map(int,I().split()))
costList = list(map(int,I().split()))
result += distance[0]*costList[0]

cheapest = costList[0]
for now in range(1,n-1):
    cheapest = min(cheapest,costList[now])
    result += cheapest*distance[now]

print(result)