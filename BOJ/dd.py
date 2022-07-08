from math import ceil


def solution(alp, cop, problems):
    n = len(problems)
    result = 0
    problems.sort(key=lambda x: -x[0])

    max_alp = problems[0][0]
    min_alp = problems[-1][0]

    problems.sort(key=lambda x: -x[1])

    max_cop = problems[0][1]
    min_cop = problems[-1][1]

    problems.sort(key=lambda x: (-(x[2] + x[3]) / x[4]))

    if alp < min_alp:
        result += (min_alp - alp)
        alp = min_alp

    if cop < min_cop:
        result += (min_cop - cop)
        cop = min_cop

    while alp < max_alp or cop < max_cop:
        for i in range(n):
            print(problems[i])
            if alp >= problems[i][0] and cop >= problems[i][1]:
                if i > 0 and (max(0,problems[i-1][0]-alp)+max(0,problems[i-1][1]-cop)) < max(0,ceil((problems[i-1][0]-alp)/problems[i][2])*problems[i][4]) + max(0,ceil((problems[i-1][1]-cop)/problems[i][3])*problems[i][4]):
                    result += (max(0, problems[i - 1][0] - alp) + max(0, problems[i - 1][1] - cop))
                    alp = problems[i - 1][0]
                    cop = problems[i - 1][1]

                else:
                    alp += problems[0][2]
                    cop += problems[0][3]
                    result += problems[0][4]

    return result

print(solution(0,0,	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
