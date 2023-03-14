from itertools import product as pro


def solution(users, emoticons):
    n = len(emoticons)
    result = [0, 0]
    nums = [10, 20, 30, 40]
    p = list(pro(nums, repeat=n))

    for i in p:
        tmp = [0, 0]
        for limit, cost in users:
            total = 0
            for k in range(len(i)):
                if i[k] >= limit:
                    total += (emoticons[k] * (100 - i[k]) // 100)

            if total >= cost:
                tmp[0] += 1

            else:
                tmp[1] += total

        result.append(tmp)

    result.sort(key=lambda x: (-x[0], -x[1]))
    return result[0]