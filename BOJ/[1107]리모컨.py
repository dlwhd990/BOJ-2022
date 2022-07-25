#https://www.acmicpc.net/problem/1107
#리모컨 [Gold 5]

import sys
from itertools import product as pro
I = sys.stdin.readline

target = int(I())
n = int(I())
broken = []
if n > 0:
    broken = list(map(int, I().split()))
possible = []
a = []
for i in range(10):
    if i not in broken:
        possible.append(i)

for i in range(1,7):
    tmp = list(pro(possible,repeat=i))
    a.extend(tmp)

result = abs(target-100)

for i in a:
    if i[0] == 0 and len(i) > 1:
        continue
    tmp = ''
    for j in i:
        tmp += str(j)

    result = min(result,len(i)+abs(target-int(tmp)))

print(result)