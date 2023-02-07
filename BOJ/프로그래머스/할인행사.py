from collections import defaultdict

def solution(want, number, discount):
    d = defaultdict(int)
    result = 0

    for i in range(10):
        d[discount[i]] += 1

    check = 0
    for j in range(len(want)):
        if d[want[j]] != number[j]:
            check = 1
            break

    if check == 0:
        result += 1

    for i in range(len(discount) - 10):
        d[discount[i]] -= 1
        d[discount[10 + i]] += 1
        check = 0
        for j in range(len(want)):
            if d[want[j]] != number[j]:
                check = 1
                break

        if check == 0:
            result += 1

    return result
