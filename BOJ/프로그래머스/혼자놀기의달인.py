def solution(cards):
    n = len(cards)
    visited = [0] * (n + 1)
    result = []
    for i in range(n):
        idx = i
        cnt = 0
        while True:
            if visited[cards[idx]] == 1:
                break

            visited[cards[idx]] = 1
            idx = (cards[idx] - 1)
            cnt += 1

        result.append(cnt)

    result.sort()
    if len(result) <= 1:
        return 0
    return result[-1] * result[-2]