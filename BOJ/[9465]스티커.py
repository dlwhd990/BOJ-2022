# 스티커 [Silver 1]
import sys
I = sys.stdin.readline

for _ in range(int(I())):
    n = int(I())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, I().split())))

    if n == 1:
        print(max(sticker[0][0],sticker[1][0]))

    else:
        d = [[0]*n for _ in range(2)]
        d[0][0] = sticker[0][0]
        d[1][0] = sticker[1][0]
        d[0][1] = max(sticker[0][0],sticker[1][0]+sticker[0][1])
        d[1][1] = max(sticker[1][0],sticker[0][0]+sticker[1][1])

        for i in range(2,n):
            d[0][i] = max(d[1][i-1],d[0][i-2],d[1][i-2]) + sticker[0][i]
            d[1][i] = max(d[0][i-1],d[0][i-2],d[1][i-2]) + sticker[1][i]


        print(max(max(d[0]),max(d[1])))