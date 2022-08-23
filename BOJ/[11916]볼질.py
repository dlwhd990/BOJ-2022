#https://www.acmicpc.net/problem/11916
#볼질 [Silver 4]
import sys
from collections import deque
I = sys.stdin.readline

n = int(I())
runs = 0
pitches = list(map(int,I().split()))
runners = deque([0,0,0])
ballCount = 0

def goToFirstBase(runners):
    result = [1,0,0]
    run = 0
    if runners[0] == 1:
        result[1] = 1

        if runners[1] == 1:
            result[2] = 1

            if runners[2] == 1:
                run = 1

        else:
            result[2] = runners[2]

    else:
        result[1] = runners[1]
        result[2] = runners[2]

    return deque(result),run

for pitch in pitches:
    if pitch == 1:
        ballCount += 1
        if ballCount == 4:
            runners, r = goToFirstBase(runners)
            runs += r
            ballCount = 0

    elif pitch == 2:
        runners, r = goToFirstBase(runners)
        runs += r
        ballCount = 0

    elif pitch == 3:
        ballCount += 1
        if ballCount == 4:
            runners.appendleft(1)
            runs += runners.pop()
            ballCount = 0

        else:
            runners.appendleft(0)
            runs += runners.pop()

print(runs)