def solution(park, routes):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    d = dict()
    d['E'] = 3
    d['S'] = 1
    d['N'] = 0
    d['W'] = 2

    n = len(park)
    m = len(park[0])
    sx = -1
    sy = -1

    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                sx = i
                sy = j
                break

        if sx != -1:
            break

    for i in routes:
        direction, cnt = i.split()
        cnt = int(cnt)
        nx = sx
        ny = sy
        check = -1

        for _ in range(cnt):
            nx += dx[d[direction]]
            ny += dy[d[direction]]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                check = 1
                break

            if park[nx][ny] == 'X':
                check = 1
                break

        if check == 1:
            continue

        sx = nx
        sy = ny

    return [sx, sy]
