#https://www.acmicpc.net/problem/12852
#1로 만들기 2

import sys
I = sys.stdin.readline

a = int(I())
if a == 1:
    print(0)
    print(1)

else:
    route = [[]for _ in range(a+1)]
    d = [int(1e10)]*(a+1)
    d[1] = 0
    d[2] = 1
    route[1].append(1)
    route[2].append(2)
    route[2].append(1)

    for i in range(2,a+1):
        if i%3 == 0:
            # d[i] = min(d[i],d[i//3]+1)
            if d[i] >= d[i//3]+1:
                route[i] = route[i//3] + [i]
                d[i] = d[i//3] + 1

        if i%2 == 0:
            # d[i] =  min(d[i],d[i//2]+1)
            if d[i] >= d[i//2]+1:
                route[i] = route[i//2] + [i]
                d[i] = d[i//2] + 1

        if i-1 > -1:
            # d[i] = min(d[i],d[i-1]+1)
            if d[i] >= d[i-1]+1:
                route[i] = route[i-1] + [i]
                d[i] = d[i-1] + 1

    print(d[a])
    route[a].sort(reverse=True)
    print(*route[a])