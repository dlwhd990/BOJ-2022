#https://www.acmicpc.net/problem/2078
#무한이진트리 [Silver 3]

import sys
I = sys.stdin.readline
a,b = map(int,I().split())
left = 0
right = 0

while a != b:
    if a > b:
        left += 1
        a -= b

    elif a < b:
        right += 1
        b -= a

print(left, right)