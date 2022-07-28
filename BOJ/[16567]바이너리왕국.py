#https://www.acmicpc.net/problem/16567
#바이너리 왕국 [Silver 3]
import sys
I = sys.stdin.readline

n,m = map(int,I().split())
ground = list(map(int,I().split()))
check = 0
cnt = 0

for i in range(n):
    if ground[i] == 1:
        if check == 0:
            check = 1

        if check == 1 and i == n-1:
            cnt += 1


    elif ground[i] == 0:
        if check == 0:
            continue

        else:
            cnt += 1
            check = 0


for _ in range(m):
    ipt = list(I().rstrip().split())
    if len(ipt) == 1:
        print(cnt)

    else:
        idx = int(ipt[1])-1
        if ground[idx] == 1:
            continue

        ground[idx] = 1

        if idx == 0 and ground[1] == 0:
            cnt += 1

        elif idx == n-1 and ground[n-2] == 0:
            cnt += 1

        elif idx > 0 and idx < n-1:
            if ground[idx-1] == 1 and ground[idx+1] == 1:
                cnt -= 1

            elif ground[idx-1] == 0 and ground[idx+1] == 0:
                cnt += 1