# 비슷한 단어 [Silver 3]
import sys
from collections import defaultdict
I = sys.stdin.readline

n = int(I())
a = I().rstrip()
result = 0



for _ in range(n-1):
    s = I().rstrip()
    d = defaultdict(int)
    t = defaultdict(int)
    check = 0
    for i in a:
        d[i] += 1

    for i in s:
        t[i] += 1

    if len(a) >= len(s):
        for i in t.keys():
            d[i] -= t[i]

        tmp = list(d.values())


    else:
        for i in d.keys():
            t[i] -= d[i]

        tmp = list(t.values())

    if tmp.count(0) == len(tmp):
        result += 1

    elif tmp.count(1) == 1 and tmp.count(0) == len(tmp) - 1:
        result += 1

    elif tmp.count(1) == 1 and tmp.count(-1) == 1 and tmp.count(0) == len(tmp) - 2:
        result += 1

print(result)