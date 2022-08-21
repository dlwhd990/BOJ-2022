#https://www.acmicpc.net/problem/18405
#경쟁적 전염 [Gold 5]

import sys
I = sys.stdin.readline

def main():
    a = []
    n, m = map(int, I().split())
    for _ in range(n):
        a.append(list(map(int, I().split())))

    s, x, y = map(int, I().split())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(s):
        tmp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j] == 0:
                    p = 1001
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                            continue

                        if a[nx][ny] == 0:
                            continue

                        p = min(p, a[nx][ny])

                    if p == 1001:
                        continue

                    tmp[i][j] = p
                    if i == x - 1 and j == y - 1:
                        print(p)
                        return

        for i in range(n):
            for j in range(n):
                if tmp[i][j] != 0:
                    a[i][j] = tmp[i][j]

    print(a[x - 1][y - 1])
    return

main()