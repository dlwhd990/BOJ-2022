import math


def solution(k, d):
    cnt = 0
    for x in range(0, 1000001, k):
        if x ** 2 > d ** 2:
            return cnt
        y = math.sqrt(d ** 2 - x ** 2)
        cnt += (y // k + 1)

    return cnt