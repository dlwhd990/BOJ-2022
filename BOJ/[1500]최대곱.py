# 최대 곱 [Silver 2]
n,m = map(int,input().split())

if n%m == 0:
    print((n//m)**m)

else:
    a = []
    result = 1

    for i in range(m):
        a.append(n//m)

    for i in range(n%m):
        a[i] += 1

    for i in a:
        result *= i

    print(result)