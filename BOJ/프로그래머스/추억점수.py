from collections import defaultdict


def solution(name, yearning, photo):
    d = defaultdict(int)
    result = []
    for i in range(len(name)):
        d[name[i]] = yearning[i]

    for i in photo:
        cnt = 0
        for j in i:
            cnt += d[j]
        result.append(cnt)

    return result