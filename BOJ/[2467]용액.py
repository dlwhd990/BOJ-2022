#https://www.acmicpc.net/problem/2467
#용액 [Gold 5]

import sys
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))
r = []
left = 0
right = n-1

while right > left:
    result = a[right]+a[left]

    r.append((abs(result),a[left],a[right]))
    if result == 0:
        break

    elif result > 0:
        right -= 1

    elif result < 0:
        left += 1

r.sort()

print(r[0][1],r[0][2])