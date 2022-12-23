# 귀여운 라이언 [Silver 1]

import sys
I = sys.stdin.readline

n,k = map(int,I().split())
a = list(map(int,I().split()))

left = 0
right = 0
cnt = 0
result = 1000001

if a[left] == 1:
    if k == 1:
        result = 1
    cnt += 1

while True:
    if cnt < k:
        right += 1
        if right >= len(a):
            break
        if a[right] == 1:
            cnt += 1

    elif cnt > k:
        if a[left] == 1:
            cnt -= 1
        left += 1


    else:
        result = min(result,right-left+1)
        if a[left] == 1:
            cnt -= 1
        left += 1


if result == 1000001:
    print(-1)
else:
    print(result)