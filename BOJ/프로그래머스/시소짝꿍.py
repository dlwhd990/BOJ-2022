def solution(weights):
    result = 0
    two = [0] * 4001
    three = [0] * 4001
    four = [0] * 4001

    for w in weights:
        two[w * 2] += 1
        three[w * 3] += 1
        four[w * 4] += 1

    for w in weights:
        result += max(two[w * 2] - 1, 0)
        result += three[w * 2]
        result += four[w * 2]
        result += two[w * 3]
        result += four[w * 3]
        result += two[w * 4]
        result += three[w * 4]

    return result // 2
