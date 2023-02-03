import heapq as hq


def solution(n, k, enemy):
    q = []
    result = 0
    enemy.reverse()

    while enemy:
        nxt = enemy.pop()
        if n - nxt < 0:
            if k == 0:
                return result
            else:
                hq.heappush(q, -nxt)
                n -= nxt
                while q and k > 0 and n < 0:
                    use = hq.heappop(q)
                    n -= use
                    k -= 1


        else:
            hq.heappush(q, -nxt)
            n -= nxt

        result += 1

    return result
