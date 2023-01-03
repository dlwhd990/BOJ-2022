# 자두나무 [Gold 5]

# d[t][w][k]
#
# T초에 w번 움직여서 k+1번 나무 아래 있을 떄 최대 값
#
# 0초에 0번 움직여서 1번나무 아래 => 0
# 0초에 1번 움직여서 2번나무 아래 => 1
# 1초에 0번 움직여서 1번나무 아래 => (0초 0번 1번)+1
# 1초에 1번 움직여서 1번나무 아래
# => 0초에 0번 움직여서 2번나무 아래

import sys
I = sys.stdin.readline

def main():
    t, w = map(int, I().split())
    d = [[[0,0]for _ in range(w+1)]for _ in range(t)]
    result = 0
    x = int(I())

    if x == 1:
        d[0][0][0] = 1

    elif x == 2:
        d[0][1][1] = 1

    for i in range(1,t):
        x = int(I())
        if x == 1:
            d[i][0][0] = d[i-1][0][0] + 1
        else:
            d[i][0][0] = d[i-1][0][0]

        if x == 2:
            d[i][0][1] = d[i-1][0][1] + 1

        else:
            d[i][0][1] = d[i-1][0][1]

        for j in range(1,w+1):
            if x == 1:
                d[i][j][0] = max(d[i-1][j-1][1],d[i-1][j][0]) + 1

            else:
                d[i][j][0] = max(d[i-1][j-1][1],d[i-1][j][0])

            if x == 2:
                d[i][j][1] = max(d[i-1][j-1][0],d[i-1][j][1]) + 1

            else:
                d[i][j][1] = max(d[i-1][j-1][0],d[i-1][j][1])



    for i in d:
        for j in i:
            result = max(result,max(j))

    return result

print(main())