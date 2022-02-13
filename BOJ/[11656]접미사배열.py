#https://www.acmicpc.net/problem/11656
#접미사 배열 [Silver 4]

import sys
I = sys.stdin.readline
a = I().rstrip()
k = []

for i in range(len(a)):
    k.append(a[len(a)-i-1:])

k.sort()
for i in k:
    print(i)