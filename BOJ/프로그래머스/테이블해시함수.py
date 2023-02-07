def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    result = -1

    for i in range(row_begin - 1, row_end):
        now = 0
        for j in data[i]:
            now += j % (i + 1)

        if result == -1:
            result = now
        else:
            result = result ^ now

    return result