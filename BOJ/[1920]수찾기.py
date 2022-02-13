#https://www.acmicpc.net/problem/1920
#수 찾기 [Silver 4]
import sys
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))
m = int(I())
b = list(map(int,I().split()))

result = [0]*m
a.sort()

for i in range(m):
    start = 0
    end = n
    while start < end:
        mid = (start+end)//2

        if a[mid] == b[i]:
            result[i] = 1
            break

        elif a[mid] > b[i]:
            end = mid

        elif a[mid] < b[i]:
            start = mid+1

for i in result:
    print(i)
