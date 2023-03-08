def solution(n, m, section):
    cnt = 0
    while section:
        cnt += 1
        now = section.pop()
        while section and section[-1] >= now - m + 1:
            section.pop()

    return cnt