def solution(today, terms, privacies):
    tmp = today.split(".")
    t = int(tmp[0]) * 28 * 12 + int(tmp[1]) * 28 + int(tmp[2])
    d = dict()
    idx = 1
    result = []

    for i in terms:
        tmp = i.split()
        d[tmp[0]] = int(tmp[1])

    for p in privacies:
        date, term = p.split()
        dateTmp = date.split(".")
        dateT = int(dateTmp[0]) * 28 * 12 + int(dateTmp[1]) * 28 + int(dateTmp[2])
        dateT += d[term] * 28
        if dateT <= t:
            result.append(idx)

        idx += 1

    return result