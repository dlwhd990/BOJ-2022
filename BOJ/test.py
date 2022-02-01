import sys
I = sys.stdin.readline

round_cnt = 0

while True:
    n,m = map(int,I().split())
    if n == 0 and m == 0:
        break

    a = []
    targets = []
    b_cnt = 0
    complete_check = 0
    round_cnt += 1
    for _ in range(n):
        ipt = list(I().rstrip())
        a.append(ipt)

    command = list(I().rstrip())

    sx = -1
    sy = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'w' or a[i][j] == 'W':
                sx = i
                sy = j

            if a[i][j] == '+' or a[i][j] == 'B' or a[i][j] == 'W':
                targets.append((i,j))

            if a[i][j] == 'b' or a[i][j] == 'B':
                b_cnt += 1


    for i in command:
        # 위
        if i == 'U':
            if a[sx-1][sy] == '.':
                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'

                a[sx-1][sy] = 'w'

                sx -= 1

            elif a[sx-1][sy] == '+':
                a[sx - 1][sy] = 'W'
                a[sx][sy] = '.'
                sx -= 1

            elif a[sx-1][sy] == 'b':
                if sx < 2 or a[sx-2][sy] == '#' or a[sx-2][sy] == 'b' or a[sx-2][sy] == 'B':
                    continue

                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'

                a[sx-1][sy] = 'w'
                if a[sx-2][sy] == '+':
                    a[sx-2][sy] = 'B'
                else:
                    a[sx-2][sy] = 'b'

                sx -= 1

            elif a[sx-1][sy] == 'B':
                if sx < 2 or a[sx-2][sy] == '#' or a[sx-2][sy] == 'b' or a[sx-2][sy] == 'B':
                    continue

                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'
                a[sx-1][sy] = 'W'
                if a[sx-2][sy] == '+':
                    a[sx-2][sy] = 'B'
                else:
                    a[sx-2][sy] = 'b'
                sx -= 1


            elif a[sx-1][sy] == '#':
                continue

        # 아래
        elif i == 'D':
            if a[sx+1][sy] == '.':
                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'

                a[sx+1][sy] = 'w'

                sx += 1

            elif a[sx+1][sy] == '+':
                a[sx+1][sy] = 'W'
                a[sx][sy] = '.'
                sx += 1

            elif a[sx+1][sy] == 'b':
                if sx > n-3 or a[sx+2][sy] == '#' or a[sx+2][sy] == 'b' or a[sx+2][sy] == 'B':
                    continue

                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'
                a[sx+1][sy] = 'w'
                if a[sx+2][sy] == '+':
                    a[sx+2][sy] = 'B'
                else:
                    a[sx+2][sy] = 'b'
                sx += 1

            elif a[sx+1][sy] == 'B':
                if sx > n-3 or a[sx+2][sy] == '#' or a[sx+2][sy] == 'b' or a[sx+2][sy] == 'B':
                    continue

                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'
                a[sx+1][sy] = 'W'
                if a[sx+2][sy] == '+':
                    a[sx+2][sy] = 'B'
                else:
                    a[sx+2][sy] = 'b'
                sx += 1


            elif a[sx+1][sy] == '#':
                continue

        #왼쪽
        elif i == 'L':
            if a[sx][sy-1] == '.':
                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'

                a[sx][sy-1] = 'w'

                sy -= 1

            elif a[sx][sy-1] == '+':
                a[sx][sy-1] = 'W'
                a[sx][sy] = '.'
                sy -= 1

            elif a[sx][sy-1] == 'b':
                if sy < 2 or a[sx][sy-2] == '#' or a[sx][sy-2] == 'b' or a[sx][sy-2] == 'B':
                    continue

                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'
                a[sx][sy-1] = 'w'
                if a[sx][sy-2] == '+':
                    a[sx][sy-2] = 'B'
                else:
                    a[sx][sy-2] = 'b'
                sy -= 1

            elif a[sx][sy-1] == 'B':
                if sy < 2 or a[sx][sy-2] == '#' or a[sx][sy-2] == 'b' or a[sx][sy-2] == 'B':
                    continue

                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'
                a[sx][sy-1] = 'W'
                if a[sx][sy-2] == '+':
                    a[sx][sy-2] = 'B'
                else:
                    a[sx][sy-2] = 'b'
                sy -= 1


            elif a[sx][sy-1] == '#':
                continue


        # 오른쪽
        elif i == 'R':
            if a[sx][sy+1] == '.':
                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'

                a[sx][sy+1] = 'w'

                sy += 1

            elif a[sx][sy+1] == '+':
                a[sx][sy+1] = 'W'
                a[sx][sy] = '.'
                sy += 1

            elif a[sx][sy+1] == 'b':
                if sy > m-3 or a[sx][sy+2] == '#' or a[sx][sy+2] == 'b' or a[sx][sy+2] == 'B':
                    continue

                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'
                a[sx][sy+1] = 'w'
                if a[sx][sy+2] == '+':
                    a[sx][sy+2] = 'B'
                else:
                    a[sx][sy+2] = 'b'
                sy += 1

            elif a[sx][sy+1] == 'B':
                if sy > m-3 or a[sx][sy+2] == '#' or a[sx][sy+2] == 'b' or a[sx][sy+2] == 'B':
                    continue

                if a[sx][sy] == 'W':
                    a[sx][sy] = '+'
                else:
                    a[sx][sy] = '.'
                a[sx][sy+1] = 'W'
                if a[sx][sy+2] == '+':
                    a[sx][sy+2] = 'B'
                else:
                    a[sx][sy+2] = 'b'
                sy += 1


            elif a[sx][sy+1] == '#':
                continue


        cnt = 0
        for i, j in targets:
            if a[i][j] == 'B':
                cnt += 1

        if cnt == b_cnt:
            complete_check = 1
            break





    print("Game %d: "%round_cnt,end='')
    if complete_check == 0:
        print("incomplete")
    else:
        print("complete")
    for i in range(n):
        for j in range(m):
            print(a[i][j],end='')
        print('')