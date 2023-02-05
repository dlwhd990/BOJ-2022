from collections import deque

p = [(3, 1)]
for i in range(3):
    for j in range(3):
        p.append((i, j))


def makeMoveCountList():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tx = [-1, -1, 1, 1]
    ty = [-1, 1, -1, 1]
    result = [[0] * 10 for _ in range(10)]

    num = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]

    for t in range(10):
        distance = [[-1] * 3 for _ in range(4)]
        sx = p[t][0]
        sy = p[t][1]
        q = deque()
        q.append((sx, sy))
        distance[sx][sy] = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > 3 or ny < 0 or ny > 2:
                    continue

                if distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 2
                    q.append((nx, ny))

            for i in range(4):
                nx = x + tx[i]
                ny = y + ty[i]

                if nx < 0 or nx > 3 or ny < 0 or ny > 2:
                    continue

                if distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 3
                    q.append((nx, ny))

        distance[sx][sy] = 1
        result[t][0] = distance[3][1]
        for i in range(3):
            for j in range(3):
                result[t][i * 3 + j + 1] = distance[i][j]

    return result


def solution(numbers):
    n = len(numbers)
    result = int(1e10)
    moveCountList = makeMoveCountList()
    distance = [[[int(1e10)] * 10 for _ in range(10)] for _ in range(n)]
    distance[0][int(numbers[0])][6] = moveCountList[4][int(numbers[0])]
    distance[0][4][int(numbers[0])] = moveCountList[6][int(numbers[0])]

    for t in range(1, n):
        x = int(numbers[t])

        for i in range(10):
            for j in range(10):
                if distance[t - 1][i][j] < int(1e10):
                    if x != j:
                        distance[t][x][j] = min(distance[t - 1][i][j] + moveCountList[i][x], distance[t][x][j])

                    if x != i:
                        distance[t][i][x] = min(distance[t - 1][i][j] + moveCountList[j][x], distance[t][i][x])

    for i in distance[-1]:
        result = min(result, min(i))

    return result



