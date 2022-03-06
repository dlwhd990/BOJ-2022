# 동전 0 [Silver 3]
import sys
I = sys.stdin.readline

n,k = map(int,I().split())
coinList = []

for _ in range(n):
    coinList.append(int(I()))

cnt = 0
current = k
for i in range(n-1,-1,-1):
    if coinList[i] > current:
        continue

    else:
        cnt += (current//coinList[i])
        current %= coinList[i]

print(cnt)