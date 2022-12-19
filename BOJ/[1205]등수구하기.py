#https://www.acmicpc.net/problem/1205
#등수 구하기 [Silver 4]
import sys
I = sys.stdin.readline

n,t,p = map(int,I().split())
if n == 0:
    print(1)
else:
    a = list(map(int,I().split()))
    a.append(t)
    a.sort(reverse=True)
    result = []

    cnt = 1
    check = 1
    for i in range(1,len(a)):
        result.append((cnt, a[i - 1]))
        if a[i-1] == a[i]:
            check += 1
            continue

        if a[i-1] != a[i] and check > 1:
            cnt += check
            check = 1
        else:
            cnt += 1

    result.append((cnt,a[-1]))

    for i in range(len(result)-1,-1,-1):
        if result[i][1] == t:
            if i >= p:
                print(-1)
                break

            else:
                print(result[i][0])
                break