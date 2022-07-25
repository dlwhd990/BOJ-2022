#https://www.acmicpc.net/problem/9095
#1,2,3 더하기 [Silver 3]
import sys
I = sys.stdin.readline

d = [0]*11
d[1] = 1
d[2] = 2
d[3] = 4
d[4] = 7
for i in range(5,11):
    d[i] = d[i-1]+d[i-2]+d[i-3]

for _ in range(int(I())):
    print(d[int(I())])