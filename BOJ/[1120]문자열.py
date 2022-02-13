#https://www.acmicpc.net/problem/1120
#문자열 [Silver 4]
import sys
I = sys.stdin.readline
a,b = I().rstrip().split()

n = len(b) - len(a)
result = int(1e10)
for i in range(n+1):
    t = b[i:len(a)+i]
    cnt = 0
    for j in range(len(a)):
        if a[j] != t[j]:
            cnt += 1

    result = min(result,cnt)

print(result)