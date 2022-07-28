#https://www.acmicpc.net/problem/1002
#터렛 [Silver 3]

import sys, math
I = sys.stdin.readline

for _ in range(int(I())):
    x1,y1,r1,x2,y2,r2 = map(int,I().split())

    dist = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

    #두 원이 동일
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    #두 원의 중심은 동일하지만 반지름이 다른 경우
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)

    #작은 원이 큰 원의 내부에 포함 되는 경우
    elif dist < max(r1,r2) - min(r1,r2):
        print(0)

    #작은 원이 큰 원의 내부에서 접하는 경우
    elif dist == max(r1,r2) - min(r1,r2):
        print(1)

    #두 원이 외부에서 접하는 경우
    elif dist == r1 + r2:
        print(1)

    #두 점에서 만나는 경우
    elif dist < r1 + r2:
        print(2)

    else:
        print(0)