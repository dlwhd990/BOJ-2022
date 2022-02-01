#https://www.acmicpc.net/problem/4577
#소코반 [Gold 3]
import sys
from collections import deque
I = sys.stdin.readline

def simulator(n,m,ground,command,cnt):
    end = 0
    boxCount = 0
    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] == "w" or ground[i][j] == "W":
                x = i
                y = j

            if ground[i][j] == 'b' or ground[i][j] == "B":
                boxCount += 1

    while command:
        dir = command.popleft()
        if dir == "U":
            if x < 1:
                continue

            if ground[x-1][y] == '#':
                continue

            if ground[x-1][y] == '.' or ground[x-1][y] == '+':
                if ground[x][y] == 'W':
                    ground[x][y] = '+'
                else:
                    ground[x][y] = '.'

                if ground[x-1][y] == '+':
                    ground[x-1][y] = 'W'
                else:
                    ground[x-1][y] = 'w'

                x -= 1

            elif ground[x-1][y] == 'b' or ground[x-1][y] == 'B':
                if x < 2:
                    continue

                if ground[x-2][y] == '#' or ground[x-2][y] == 'b' or ground[x-2][y] == "B":
                    continue

                if ground[x-2][y] == '.':
                    ground[x-2][y] = 'b'

                elif ground[x-2][y] == '+':
                    ground[x-2][y] = 'B'

                if ground[x-1][y] == 'B':
                    ground[x-1][y] = 'W'

                else:
                    ground[x-1][y] = 'w'

                if ground[x][y] == 'W':
                    ground[x][y] = '+'

                else:
                    ground[x][y] = '.'

                x -= 1

        elif dir == "D":
            if x > n-2:
                continue

            if ground[x+1][y] == '#':
                continue

            if ground[x+1][y] == '.' or ground[x+1][y] == '+':
                if ground[x][y] == 'W':
                    ground[x][y] = '+'
                else:
                    ground[x][y] = '.'

                if ground[x+1][y] == '+':
                    ground[x+1][y] = 'W'
                else:
                    ground[x+1][y] = 'w'

                x += 1

            elif ground[x+1][y] == 'b' or ground[x+1][y] == 'B':
                if x > n-3:
                    continue

                if ground[x+2][y] == '#' or ground[x+2][y] == 'b' or ground[x+2][y] == "B":
                    continue

                if ground[x+2][y] == '.':
                    ground[x+2][y] = 'b'

                elif ground[x+2][y] == '+':
                    ground[x+2][y] = 'B'

                if ground[x+1][y] == 'B':
                    ground[x+1][y] = 'W'

                else:
                    ground[x+1][y] = 'w'

                if ground[x][y] == 'W':
                    ground[x][y] = '+'

                else:
                    ground[x][y] = '.'

                x += 1

        elif dir == "L":
            if y < 1:
                continue

            if ground[x][y-1] == '#':
                continue

            if ground[x][y-1] == '.' or ground[x][y-1] == '+':
                if ground[x][y] == 'W':
                    ground[x][y] = '+'
                else:
                    ground[x][y] = '.'

                if ground[x][y-1] == '+':
                    ground[x][y-1] = 'W'
                else:
                    ground[x][y-1] = 'w'

                y -= 1

            elif ground[x][y-1] == 'b' or ground[x][y-1] == 'B':
                if y < 2:
                    continue

                if ground[x][y-2] == '#' or ground[x][y-2] == 'b' or ground[x][y-2] == "B":
                    continue


                if ground[x][y-2] == '.':
                    ground[x][y-2] = 'b'

                elif ground[x][y-2] == '+':
                    ground[x][y-2] = 'B'

                if ground[x][y-1] == 'B':
                    ground[x][y-1] = 'W'

                else:
                    ground[x][y-1] = 'w'

                if ground[x][y] == 'W':
                    ground[x][y] = '+'

                else:
                    ground[x][y] = '.'

                y -= 1

        elif dir == "R":
            if y > m-2:
                continue

            if ground[x][y+1] == '#':
                continue

            if ground[x][y+1] == '.' or ground[x][y+1] == '+':
                if ground[x][y] == 'W':
                    ground[x][y] = '+'
                else:
                    ground[x][y] = '.'

                if ground[x][y+1] == '+':
                    ground[x][y+1] = 'W'
                else:
                    ground[x][y+1] = 'w'

                y += 1

            elif ground[x][y+1] == 'b' or ground[x][y+1] == 'B':
                if y > m-3:
                    continue

                if ground[x][y+2] == '#' or ground[x][y+2] == 'b' or ground[x][y+2] == "B":
                    continue

                if ground[x][y+2] == '.':
                    ground[x][y+2] = 'b'

                elif ground[x][y+2] == '+':
                    ground[x][y+2] = 'B'

                if ground[x][y+1] == 'B':
                    ground[x][y+1] = 'W'

                else:
                    ground[x][y+1] = 'w'

                if ground[x][y] == 'W':
                    ground[x][y] = '+'

                else:
                    ground[x][y] = '.'

                y += 1


        end = 0
        for i in range(n):
            for j in range(m):
                if ground[i][j] == "B":
                    end += 1

        if end == boxCount:
            print("Game {0}: complete".format(cnt))
            for p in ground:
                print(''.join(p))
            break



    if end != boxCount:
        print("Game {0}: incomplete".format(cnt))
        for p in ground:
            print(''.join(p))




cnt = 0

while True:
    cnt += 1
    n,m = map(int,I().split())
    if n == 0 or m == 0:
        break

    ground = []
    for _ in range(n):
        ground.append(list(I().rstrip()))

    command = deque(list(I().rstrip()))

    simulator(n,m,ground,command,cnt)


