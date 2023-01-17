# 스위치 켜고 끄기 [Silver 4]
import sys
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))
for _ in range(int(I())):
    x,y = map(int,I().split())

    if x == 1:
        idx = y
        while idx-1 < n:
            a[idx-1] = abs(a[idx-1]-1)
            idx += y

    elif x == 2:
        idx = 1
        a[y-1] = abs(a[y-1]-1)
        while y-1-idx >= 0 and y-1+idx < n:
            if a[y-1-idx] == a[y-1+idx]:
                a[y-1-idx] = a[y-1+idx] = abs(a[y-1-idx]-1)
                idx += 1
            else:
                break

for i in range(n):
    print(a[i],end='')
    if (i+1)%10 == 0:
        print("")
    else:
        print(' ',end='')