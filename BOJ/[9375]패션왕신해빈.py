#https://www.acmicpc.net/problem/9375
#패션왕 신해빈 [Silver 3]
import sys
I = sys.stdin.readline

for _ in range(int(I())):
    d = dict()
    result = 1
    for _ in range(int(I())):
        tmp = list(I().rstrip().split())
        if tmp[1] not in d.keys():
            d[tmp[1]] = 2
        else:
            d[tmp[1]] += 1

    t = list(d.values())
    for i in t:
        result *= i

    print(result-1)