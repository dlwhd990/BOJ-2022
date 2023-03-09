# [-2,3,6,1,-3,-1,-2,4]
# [-2,1,7,8,5,4,2,6]
# [2,-3,-6,-1,3,1,2,-4]
# [2,-1,-7,-8,-5,-4,-2,-6]
def solution(sequence):
    r = [0]
    n = len(sequence)
    for i in range(n):
        if i % 2 == 0:
            r.append(r[-1] - sequence[i])
        else:
            r.append(r[-1] + sequence[i])

    return abs(max(r) - min(r))