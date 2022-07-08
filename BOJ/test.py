from collections import deque


def solution(alp, cop, problems):
    result = 0
    problems.sort(key=lambda x: -x[0])

    max_alp = problems[0][0]

    problems.sort(key=lambda x: -x[1])

    max_cop = problems[0][1]

    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    def sorter():
        if max_alp - alp >= max_cop - cop:
            if alp <= cop:
                problems.sort(key=lambda x: (-x[2] / x[4], -x[3] / x[4], x[0], x[1]))

            elif alp > cop:
                problems.sort(key=lambda x: (-x[2] / x[4], -x[3] / x[4], x[1], x[0]))

        else:
            if alp <= cop:
                problems.sort(key=lambda x: (-x[3] / x[4], -x[2] / x[4], x[0], x[1]))

            elif alp > cop:
                problems.sort(key=lambda x: (-x[3] / x[4], -x[2] / x[4], x[1], x[0]))

    sorter()
    while alp < max_alp and cop < max_cop:
        problems = deque(problems)
        now = problems.popleft()
        if now[0] <= alp and now[1] <= cop:
            alp += now[2]
            cop += now[3]
            result += now[4]
            problems = list(problems)
            sorter()

        problems.append(now)

    return result


print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))