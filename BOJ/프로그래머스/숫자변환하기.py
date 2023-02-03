from collections import deque


def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    visited = [0] * 1000001
    while q:
        now, dist = q.popleft()
        if now == y:
            return dist

        if now * 3 <= y and visited[now * 3] == 0:
            visited[now * 3] = 1
            q.append((now * 3, dist + 1))

        if now * 2 <= y and visited[now * 2] == 0:
            visited[now * 2] = 1
            q.append((now * 2, dist + 1))

        if now + n <= y and visited[now + n] == 0:
            visited[now + n] = 1
            q.append((now + n, dist + 1))

    return -1
