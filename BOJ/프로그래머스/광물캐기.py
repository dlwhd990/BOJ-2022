def solution(picks, minerals):
    result = 0
    p = []
    total = sum(picks)

    for i in range(0, min(len(minerals), total * 5), 5):
        tmp = [0, 0, 0]
        for j in minerals[i:i + 5]:
            if j == 'diamond':
                tmp[0] += 1
            elif j == 'iron':
                tmp[1] += 1
            else:
                tmp[2] += 1

        p.append(tmp)

    p.sort(key=lambda x: (x[0], x[1]))

    while p:
        nxt = p.pop()
        if picks[0] > 0:
            picks[0] -= 1
            result += sum(nxt)

        elif picks[1] > 0:
            picks[1] -= 1
            result += nxt[0] * 5
            result += (nxt[1] + nxt[2])

        elif picks[2] > 0:
            picks[2] -= 1
            result += nxt[0] * 25
            result += nxt[1] * 5
            result += nxt[2]

    return result

