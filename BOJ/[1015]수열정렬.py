# 수열정렬 [Silver 4]
import sys
I = sys.stdin.readline
n = int(I())
a = list(map(int,I().split()))
b = []
result = [0]*n

for i in range(n):
    b.append((a[i],i))

b.sort()

for i in range(n):
    result[b[i][1]] = i

print(*result)