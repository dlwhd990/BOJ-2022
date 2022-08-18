#https://www.acmicpc.net/problem/22251
#빌런 호석 [Gold 5]

import sys
from itertools import product as pro
I = sys.stdin.readline

n,k,p,x = map(int,I().split())
result = 0

a = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2], [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], [3, 5, 0, 2, 5, 4, 3, 4, 2, 3], [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], [3, 5, 4, 2, 3, 0, 1, 4, 2, 1], [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], [1, 5, 2, 2, 3, 2, 1, 4, 0, 1], [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]
possible = list(pro([str(i) for i in range(10)],repeat=k))
start = str(x).zfill(k)

for i in possible:
    target = int(''.join(list(i)))
    if  target > n or target == 0:
        continue
    score = 0
    for j in range(len(i)):
        score += a[int(start[j])][int(i[j])]

    if score > p:
        continue

    result += 1

print(result-1)