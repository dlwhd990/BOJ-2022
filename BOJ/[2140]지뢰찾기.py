#지뢰찾기 [Gold 4]
import sys
I = sys.stdin.readline

def main():
    result = 0
    board = []
    n = int(I())
    for _ in range(n):
        board.append(list(I().rstrip()))

    if n <= 2:
        return 0

    if n == 3:
        if int(board[0][0]) >= 1:
            return 1
        return 0

    # 모서리 처리
    if int(board[0][0]) >= 1:
        board[1][1] = "O"
    else:
        board[1][1] = "X"

    if int(board[-1][0]) >= 1:
        board[-2][1] = "O"
    else:
        board[-2][1] = "X"

    if int(board[0][-1]) >= 1:
        board[1][-2] = "O"
    else:
        board[1][-2] = "X"

    if int(board[-1][-1]) >= 1:
        board[-2][-2] = "O"
    else:
        board[-2][-2] = "X"

    # n=4이면 모서리 처리만으로 끝
    if n == 4:
        return board[1].count('O') + board[-2].count('O')


    for i in range(1,n-2):
        need = int(board[0][i])
        for j in range(i-1,i+1):
            if board[1][j] == 'O':
                need -= 1

        if need == 0:
            board[1][i+1] = 'X'
        elif need == 1:
            board[1][i+1] = 'O'


    for i in range(1, n-2):
        need = int(board[-1][i])

        for j in range(i - 1, i + 1):
            if board[-2][j] == 'O':
                need -= 1

        if need == 0:
            board[-2][i + 1] = 'X'
        elif need == 1:
            board[-2][i + 1] = 'O'


    for i in range(1, n - 3):
        need = int(board[i][0])

        for j in range(i - 1, i + 1):
            if board[j][1] == 'O':
                need -= 1

        if need == 0:
            board[i+1][1] = 'X'
        elif need == 1:
            board[i+1][1] = 'O'


    for i in range(1, n - 3):
        need = int(board[i][-1])

        for j in range(i - 1, i + 1):
            if board[j][-2] == 'O':
                need -= 1

        if need == 0:
            board[i+1][-2] = 'X'
        elif need == 1:
            board[i+1][-2] = 'O'


    for i in board:
        for j in i:
            if j == 'O' or j == '#':
                result += 1


    return result


print(main())