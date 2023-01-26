# 1. 게임판은 4가지 형태로 존재할 수 있다. (400만)
# 2. 게임판의 위치에 따라, 최종적으로 떨어지는 자리를 미리 구해서 저장해놓는다 (1번의 4가지 경우 모두, 400만)
# 3. 공의 첫 위치를 좌표로 저장하고, 게임판에서 지운다.
# 4. 게임판을 회전하면, 현재 공의 좌표도 그에 맞게 수정하고 2번의 결과에 따라 좌표를 변경한다.

import sys
I = sys.stdin.readline

n,k = map(int,I().split())
original = []
board = []
fallPoint = []
ball = [-1,-1]
now = 0
for _ in range(n):
    original.append(list(I().rstrip()))

for i in range(n):
    for j in range(n):
        if original[i][j] == 'L':
            original[i][j] = '.'
            ball = [i,j]
            break

board.append(original)

for _ in range(4):
    tmp = [['.']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = board[-1][n-1-j][i]

    board.append(tmp)


for t in range(4):
    tmp = [[-1]*n for _ in range(n)]
    for j in range(n):
        destination = n
        for i in range(n-1,-1,-1):
            if board[t][i][j] == 'X':
                destination = i

            else:
                tmp[i][j] = destination-1

    fallPoint.append(tmp)

for _ in range(k):
    query = I().rstrip()

    if query == 'L':
        if now == 0:
            now = 3
        else:
            now -= 1

        ball = [n-1-ball[1],ball[0]]


    elif query == 'D':
        if now == 3:
            now = 0
        else:
            now += 1

        ball = [ball[1], n-1-ball[0]]

    ball = [fallPoint[now][ball[0]][ball[1]],ball[1]]

result = board[now]

for i in range(n):
    for j in range(n):
        if ball[0] == i and ball[1] == j:
            print("L",end='')
        else:
            print(result[i][j],end="")

    print("")