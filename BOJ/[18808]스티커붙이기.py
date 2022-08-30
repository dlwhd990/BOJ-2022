#https://www.acmicpc.net/problem/18808
#스티커 붙이기 [Gold 3]

#보류
import sys
I = sys.stdin.readline

def turn(sticker):
    tmp = []
    for i,j in sticker:
        tmp.append((j,-i))

    return tmp



n,m,k = map(int,I().split())
board = [[0] * m for _ in range(n)]
s = []
result = 0

for _ in range(k):
    x,y = map(int,I().split())
    tmp = []

    for _ in range(x):
        tmp.append(list(map(int,I().split())))

    sticker = []
    for i in range(x):
        for j in range(y):
            if tmp[i][j] == 1:
                sticker.append((i,j))

    s.append(sticker)

for t in range(k):
    sticker = s[t] + []
    attached = 0
    for p in range(4):
        for i in range(n):
            for j in range(m):
                check = 0
                for dx, dy in sticker:
                    nx = i + dx
                    ny = j + dy

                    if (nx > n - 1 or ny > m - 1 or nx < 0 or ny < 0) or board[nx][ny] == 1:
                        check = 1
                        break

                if check == 0:
                    for dx, dy in sticker:
                        nx = i + dx
                        ny = j + dy

                        board[nx][ny] = 1
                        attached = 1

                    break

            if attached == 1:
                break

        if attached == 1:
            break

        sticker = turn(sticker)


for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            result += 1

print(result)



