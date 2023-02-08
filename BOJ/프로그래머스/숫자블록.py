import math


def getMax(n):
    if n == 1:
        return 0
    result = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i <= 10000000:
                result = max(result, n // i)

    return result


def solution(begin, end):
    d = dict()

    for i in range(end, begin - 1, -1):
        d[i] = getMax(i)

    result = [i for i in d.values()]
    result.reverse()
    return result
