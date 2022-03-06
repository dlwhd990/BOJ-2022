# 내려가기 [Gold 4]
import sys
I = sys.stdin.readline

n = int(I())
board = []
maxd = [0]*3
maxtmp = [0]*3
mind = [int(1e10)]*3
mintmp = [int(1e10)]*3

for i in range(n):
    board = list(map(int,I().split()))
    if i == 0:
        for j in range(3):
            maxtmp[j] = board[j]
            mintmp[j] = board[j]

    else:

        maxd[0] = board[0] + max(maxtmp[0], maxtmp[1])
        maxd[1] = board[1] + max(maxtmp)
        maxd[2] = board[2] + max(maxtmp[1], maxtmp[2])
        mind[0] = board[0] + min(mintmp[0], mintmp[1])
        mind[1] = board[1] + min(mintmp)
        mind[2] = board[2] + min(mintmp[1], mintmp[2])

        for j in range(3):
            maxtmp[j] = maxd[j]
            mintmp[j] = mind[j]

if n == 1:
    print(max(board),min(board))

else:
    print(max(maxd),min(mind))