def solution(sequence):
    r = [0]
    n = len(sequence)
    for i in range(n):
        if i % 2 == 0:
            r.append(r[-1] - sequence[i])
        else:
            r.append(r[-1] + sequence[i])

    return abs(max(r) - min(r))