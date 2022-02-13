#https://www.acmicpc.net/problem/2805
#나무 자르기 [Silver 3]
import sys
I = sys.stdin.readline

n,m = map(int,I().split())
a = list(map(int,I().split()))

start = 0
end = max(a)

result = -1
mid = 0

while start < end:
    mid = (start+end)//2

    tmpResult = 0
    for i in range(n):
        if (a[i]-mid) > 0:
            tmpResult += (a[i]-mid)

    if tmpResult == m:
        result = mid
        break
    elif tmpResult > m:
        result = mid
        start = mid+1

    elif tmpResult < m:
        end = mid

print(result)