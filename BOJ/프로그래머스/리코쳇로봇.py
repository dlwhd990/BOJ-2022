from collections import deque


def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(board)
    m = len(board[0])
    sx = -1
    sy = -1

    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        board[i] = list(board[i])

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                board[i][j] = '.'
                sx = i
                sy = j
                break

        if sx != -1:
            break

    q = deque()
    q.append((sx, sy, 1))

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]

                if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                    nx -= dx[i]
                    ny -= dy[i]
                    if visited[nx][ny] != 0:
                        break

                    visited[nx][ny] = 1
                    if board[nx][ny] == 'G':
                        return cnt

                    q.append((nx, ny, cnt + 1))
                    break

                if board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]

                    if visited[nx][ny] != 0:
                        break

                    visited[nx][ny] = 1

                    if board[nx][ny] == 'G':
                        return cnt

                    q.append((nx, ny, cnt + 1))
                    break

    return -1




