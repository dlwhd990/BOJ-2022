#https://www.acmicpc.net/problem/16722
#결! 합! [Gold 4]

import sys
I = sys.stdin.readline

pocket = []
for _ in range(9):
    pocket.append(list(I().rstrip().split()))

haps = []
history = []
result = 0
cnt = 0

for i in range(9):
    for j in range(i+1,9):
        for k in range(j+1,9):
            cnt = 0
            x,y,z = pocket[i],pocket[j],pocket[k]

            if x[0] == y[0] == z[0]:
                cnt += 1

            elif x[0] != y[0] and y[0] != z[0] and x[0] != z[0]:
                cnt += 1

            if x[1] == y[1] == z[1]:
                cnt += 1


            elif x[1] != y[1] and y[1] != z[1] and x[1] != z[1]:

                cnt += 1

            if x[2] == y[2] == z[2]:
                cnt += 1


            elif x[2] != y[2] and y[2] != z[2] and x[2] != z[2]:

                cnt += 1

            if cnt == 3:
                haps.append((i+1,j+1,k+1))


gCheck = 0

for _ in range(int(I())):
    ipt = list(I().rstrip().split())
    if ipt[0] == "G":
        if len(history) == len(haps):
            if gCheck == 1:
                result -= 1
            else:
                result += 3
                gCheck = 1
        else:
            result -= 1

        continue

    ipt = ipt[1:]
    ipt.sort()

    hapCom = (int(ipt[0]), int(ipt[1]), int(ipt[2]))

    if  hapCom in haps and hapCom not in history:
        result += 1
        history.append(hapCom)

    else:
        result -= 1


print(result)